import asyncio
import json
import logging
import logging.handlers
import re
import time
import unittest
from functools import wraps
from typing import Callable, Optional
from dataclasses import dataclass, field


# ============================================
# CUSTOM EXCEPTIONS
# ============================================

class RouteNotFoundError(Exception):
    """Raised when a requested command or route is not found."""
    pass


class InvalidRequestError(Exception):
    """Raised when the request format or JSON payload is invalid."""
    pass


class MiddlewareError(Exception):
    """Raised when a middleware rejects the request and prevents it from proceeding."""
    pass


# ============================================
# REQUEST / RESPONSE OBJECTS (dataclasses)
# ============================================

@dataclass
class Request:
    """Represents a single incoming client request."""
    command: str                          # e.g., "path" (e.g., "create_task")
    payload: dict                         # Data sent with the request
    params: dict = field(default_factory=dict)  # Path parameters extracted from the command
    client_addr: tuple = None             # IP and port of the client
    timestamp: float = None               # Time when the request was received

    def get(self, key: str, default=None):
        """Retrieves a value from the request payload with an optional default."""
        return self.payload.get(key, default)

# ============================================
# USAGE EXAMPLE FOR REQUEST:
# req = Request(command="ping", payload={"name": "Ali"})
# 
# # What the user writes to use it:
# user_name = req.get("name", "Unknown") 
# # -> Returns: "Ali"
#
# user_age = req.get("age", 20)
# # -> Returns: 20 (since 'age' was not in the payload)
# ============================================


@dataclass
class Response:
    """Represents the response to be sent back to the client."""
    body: dict
    status: str = "ok"    # "ok" / "error"
    code: int = 200

    @classmethod
    def success(cls, data: dict):
        """Factory method to create a success response."""
        return cls(body={"data": data}, status="ok", code=200)

    @classmethod
    def error(cls, message: str, code: int = 400):
        """Factory method to create an error response."""
        return cls(body={"error": message}, status="error", code=code)

    def to_json(self) -> str:
        """Serializes the Response object to a JSON string for TCP transmission."""
        return json.dumps({
            "status": self.status,
            "code": self.code,
            "body": self.body
        })

# ============================================
# USAGE EXAMPLE FOR RESPONSE:
# 
# # What the user writes to use it (Success):
# success_res = Response.success({"id": 1}) 
# # -> Returns: Response(body={'data': {'id': 1}}, status='ok', code=200)
#
# # What the user writes to use it (Error):
# error_res = Response.error("Not Found", 404)
# # -> Returns: Response(body={'error': 'Not Found'}, status='error', code=404)
#
# # What the server uses internally to send to client:
# json_str = success_res.to_json()
# # -> Returns: '{"status": "ok", "code": 200, "body": {"data": {"id": 1}}}'
# ============================================


# ============================================
# HTTP-LIKE PARSER (parse raw bytes → Request)
# ============================================

class RequestParser:
    """A manual parser that takes raw bytes and converts them into a Request object."""

    @staticmethod
    def parse(raw_data: bytes, client_addr: tuple) -> Request:
        """
        Decodes bytes to a JSON string, then into a Request object.
        Expected format: {"command": "...", "payload": {...}}
        Raises InvalidRequestError if the format is incorrect.
        """
        try:
            data = json.loads(raw_data.decode('utf-8'))
            if "command" not in data or "payload" not in data:
                raise InvalidRequestError("Missing 'command' or 'payload'")
            return Request(
                command=data["command"],
                payload=data["payload"],
                client_addr=client_addr,
                timestamp=time.time()
            )
        except json.JSONDecodeError:
            raise InvalidRequestError("Invalid JSON format")
        except UnicodeDecodeError:
            raise InvalidRequestError("Payload must be UTF-8 encoded")

# ============================================
# USAGE EXAMPLE FOR REQUEST PARSER:
# 
# # What the user writes to use it:
# raw_bytes = b'{"command": "hello", "payload": {"name": "Ali"}}'
# req = RequestParser.parse(raw_bytes, ("127.0.0.1", 5000))
# # -> Returns a Request object: Request(command='hello', payload={'name': 'Ali'}, ...)
# ============================================


# ============================================
# ROUTER (Decorator-based routing)
# ============================================

class Router:
    """Registers commands/routes and dispatches requests to the appropriate handlers."""

    def __init__(self):
        self._routes: dict[str, Callable] = {}
        self._dynamic_routes: list = []  # regex-based routes with parameters like {params}

    def route(self, command: str):
        """
        Decorator for routing - e.g., @router.route("create_task").
        Registers a function as the handler for a specific command.
        
        Example:
            @app.route("ping")
            async def ping_handler(request: Request) -> Response:
                return Response.success({"message": "pong"})
        """
        def decorator(func):
            self._routes[command] = func
            @wraps(func)
            async def wrapper(*args, **kwargs):
                return await func(*args, **kwargs)
            return wrapper
        return decorator

    def route_dynamic(self, pattern: str):
        """
        Decorator for routes with dynamic parameters.
        For example: "task/{task_id}/status".
        Uses regex to extract values and puts them in request.params.
        
        Example:
            @app.route_dynamic("user/{user_id}/profile")
            async def get_user(request: Request) -> Response:
                user_id = request.params.get("user_id")
                return Response.success({"user_id": user_id})
        """
        def decorator(func):
            regex_pattern = re.sub(r'\{([^}]+)\}', r'(?P<\1>[^/]+)', pattern)
            regex = re.compile(f"^{regex_pattern}$")
            self._dynamic_routes.append((regex, func))
            @wraps(func)
            async def wrapper(*args, **kwargs):
                return await func(*args, **kwargs)
            return wrapper
        return decorator

    async def dispatch(self, request: Request) -> Response:
        """
        Finds the appropriate handler for request.command.
        Calls the handler asynchronously and returns a Response.
        Raises RouteNotFoundError if no handler is found.
        """
        if request.command in self._routes:
            return await self._routes[request.command](request)
        
        match = self._match_dynamic_route(request.command)
        if match:
            func, params = match
            request.params.update(params)
            return await func(request)
            
        raise RouteNotFoundError(f"Route '{request.command}' not found")

    def _match_dynamic_route(self, command: str) -> Optional[tuple]:
        """Helper function that matches a command against dynamic routes using regex."""
        for regex, func in self._dynamic_routes:
            match = regex.match(command)
            if match:
                return func, match.groupdict()
        return None

# ============================================
# USAGE EXAMPLE FOR ROUTER:
# 
# router = Router()
#
# # What the user writes to register a simple route:
# @router.route("ping")
# async def ping(req: Request) -> Response:
#     return Response.success({"msg": "pong"})
# # -> Returns: Registers 'ping' command to ping() function.
#
# # What the user writes to register a dynamic route:
# @router.route_dynamic("user/{id}")
# async def get_user(req: Request) -> Response:
#     return Response.success({"user": req.params.get("id")})
# # -> Returns: Registers 'user/{id}' pattern. If client sends "user/123", req.params will have {"id": "123"}.
# ============================================


# ============================================
# MIDDLEWARE SYSTEM
# ============================================

class Middleware:
    """
    Base class (interface) that all middleware components should inherit from.
    
    Example:
        class CustomHeaderMiddleware(Middleware):
            async def after_request(self, request: Request, response: Response) -> Response:
                # Modify response body before sending
                response.body["custom_header"] = "MyFramework-v1"
                return response
    """

    async def before_request(self, request: Request) -> Optional[Request]:
        """
        Executed before the request reaches the handler.
        Can modify the request or raise an error to reject it.
        """
        return request

    async def after_request(self, request: Request, response: Response) -> Response:
        """Executed after the handler returns a response, allowing for modification of the response."""
        return response


class LoggingMiddleware(Middleware):
    """Middleware that logs information about every incoming request and outgoing response."""

    async def before_request(self, request: Request) -> Request:
        """Logs details of the incoming request such as command and timestamp."""
        logging.info(f"Incoming: '{request.command}' from {request.client_addr}")
        return request

    async def after_request(self, request: Request, response: Response) -> Response:
        """Logs the result of the request processing, including status, code, and duration."""
        logging.info(f"Outgoing: status={response.status} code={response.code}")
        return response


class TimingMiddleware(Middleware):
    """Middleware that measures the time taken to process a request."""

    async def before_request(self, request: Request) -> Request:
        """Records the start timestamp in request.timestamp."""
        request.timestamp = time.time()
        return request

    async def after_request(self, request: Request, response: Response) -> Response:
        """Calculates and logs the time difference between request start and response completion."""
        duration = time.time() - request.timestamp
        logging.info(f"Request took {duration:.4f}s")
        return response


class AuthMiddleware(Middleware):
    """Middleware that verifies if the request contains a valid authentication token."""

    def __init__(self, valid_tokens: set):
        self._valid_tokens = valid_tokens

    async def before_request(self, request: Request) -> Request:
        """
        Checks if the request payload contains a valid token.
        Raises MiddlewareError if the token is missing or invalid.
        """
        token = request.payload.get("token")
        if token not in self._valid_tokens:
            raise MiddlewareError("Invalid or missing authentication token")
        return request


class MiddlewareManager:
    """Manages a list of middleware and applies them in the correct order."""

    def __init__(self):
        self._middlewares: list[Middleware] = []

    def add(self, middleware: Middleware) -> None:
        """Adds a new middleware to the list."""
        self._middlewares.append(middleware)

    async def run_before(self, request: Request) -> Request:
        """
        Executes all before_request methods in the order they were added (middleware1 → middleware2 → ...).
        """
        for mw in self._middlewares:
            request = await mw.before_request(request)
            if request is None:
                raise MiddlewareError("Request rejected by middleware (returned None)")
        return request

    async def run_after(self, request: Request, response: Response) -> Response:
        """
        Executes all after_request methods in reverse order.
        """
        for mw in reversed(self._middlewares):
            response = await mw.after_request(request, response)
        return response

# ============================================
# USAGE EXAMPLE FOR MIDDLEWARE & MANAGER:
# 
# # What the user writes to create a Custom Middleware:
# class MyMiddleware(Middleware):
#     async def before_request(self, req: Request) -> Request:
#         print("Request is starting!")
#         return req  # Must return the Request object
#
# # What the user writes to use it:
# manager = MiddlewareManager()
# manager.add(MyMiddleware())
# # -> Returns: None. Adds MyMiddleware to the list of middlewares.
# ============================================


# ============================================
# LOGGER CONFIGURATION
# ============================================

def setup_logger(name: str, log_file: str, level=logging.INFO) -> logging.Logger:
    """
    Configures a logger with file rotation (using RotatingFileHandler).
    Returns a ready-to-use logger instance.
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)
    if not logger.handlers:
        handler = logging.handlers.RotatingFileHandler(log_file, maxBytes=1048576, backupCount=3)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    return logger


# ============================================
# ERROR HANDLER DECORATOR
# ============================================

class ErrorHandlerRegistry:
    """Registers and manages custom handlers for different exception types."""

    def __init__(self):
        self._handlers: dict[type, Callable] = {}

    def register(self, exception_type: type, handler: Callable) -> None:
        """Registers a new handler for a specific exception type."""
        self._handlers[exception_type] = handler

    async def handle(self, exception: Exception, request: Request) -> Response:
        """
        Finds the appropriate handler for the given exception.
        Returns a generic error Response if no specific handler is found.
        """
        exc_type = type(exception)
        handler = self._handlers.get(exc_type)
        if handler:
            return await handler(exception, request)
        return Response.error(f"Internal server error: {str(exception)}", 500)

# ============================================
# USAGE EXAMPLE FOR ERROR HANDLER REGISTRY:
# 
# registry = ErrorHandlerRegistry()
#
# # What the user writes to define an error handler:
# async def handle_bad_json(e: Exception, req: Request) -> Response:
#     return Response.error("Bad JSON format!", 400)
#
# # What the user writes to register it:
# registry.register(InvalidRequestError, handle_bad_json)
# # -> Returns: None. Now whenever InvalidRequestError happens, handle_bad_json runs!
# ============================================


# ============================================
# ASYNC TCP SERVER (le coeur dyal l'app)
# ============================================

class TaskQueueServer:
    """The main asynchronous TCP server that coordinates the router, middleware, and error handling."""

    def __init__(self, host: str, port: int):
        self._host = host
        self._port = port
        self.router = Router()
        self.middleware_manager = MiddlewareManager()
        self.error_registry = ErrorHandlerRegistry()
        self.logger = None  # Will be initialized with setup_logger()

    def error_handler(self, exception_type: type):
        """
        Decorator factory that registers a custom handler for a specific exception type.
        
        Example:
            @app.error_handler(RouteNotFoundError)
            async def handle_not_found(e: Exception, req: Request) -> Response:
                return Response.error("Sorry, that command does not exist!", 404)
        """
        def decorator(func):
            self.error_registry.register(exception_type, func)
            @wraps(func)
            async def wrapper(*args, **kwargs):
                return await func(*args, **kwargs)
            return wrapper
        return decorator

    async def handle_client(self, reader: asyncio.StreamReader, 
                             writer: asyncio.StreamWriter) -> None:
        """
        Handles a new client connection.
        1. Reads raw data from the reader.
        2. Parses it using RequestParser.
        3. Executes middleware run_before().
        4. Dispatches the request via router.
        5. Executes middleware run_after().
        6. Writes the response back to the writer.
        7. Uses try/except to catch errors and pass them to error_registry.
        """
        client_addr = writer.get_extra_info('peername')
        request_obj = Request(command="unknown", payload={}, client_addr=client_addr)
        
        if self.logger:
            self.logger.info(f"New connection from {client_addr}")
            
        try:
            raw_data = await reader.read(4096)
            if not raw_data:
                return

            request_obj = RequestParser.parse(raw_data, client_addr)
            request_obj = await self.middleware_manager.run_before(request_obj)
            response = await self.router.dispatch(request_obj)
            response = await self.middleware_manager.run_after(request_obj, response)

        except Exception as e:
            response = await self.error_registry.handle(e, request_obj)
            if self.logger:
                self.logger.error(f"Error handling request: {e}")

        writer.write(response.to_json().encode('utf-8'))
        await writer.drain()
        writer.close()
        await writer.wait_closed()

    def route(self, command: str):
        """Shortcut method that delegates to router.route()."""
        return self.router.route(command)

    def route_dynamic(self, pattern: str):
        """Shortcut method that delegates to router.route_dynamic()."""
        return self.router.route_dynamic(pattern)

    def use_middleware(self, middleware: Middleware) -> None:
        """Shortcut method that delegates to middleware_manager.add()."""
        self.middleware_manager.add(middleware)

    async def start(self) -> None:
        """
        Starts listening for connections using asyncio.start_server().
        Runs the event loop indefinitely (serve_forever).
        """
        self.logger = setup_logger("TaskQueueServer", "server.log")
        server = await asyncio.start_server(self.handle_client, self._host, self._port)
        self.logger.info(f"Server started on {self._host}:{self._port}")
        
        async with server:
            await server.serve_forever()

    def run(self) -> None:
        """Entry point that calls asyncio.run(self.start())."""
        try:
            asyncio.run(self.start())
        except KeyboardInterrupt:
            if self.logger:
                self.logger.info("Server stopped.")

# ============================================
# USAGE EXAMPLE FOR TASK QUEUE SERVER:
# 
# # What the user writes to create the server:
# app = TaskQueueServer("127.0.0.1", 8080)
#
# # What the user writes to add routes directly to the server:
# @app.route("test")
# async def test(req: Request) -> Response:
#     return Response.success({"ok": True})
#
# # What the user writes to start the server:
# # app.run() 
# # -> Returns: None. It runs forever, listening for connections on 127.0.0.1:8080!
# ============================================


# ============================================
# CLIENT SIMULATOR (باش تجرب السيرفر بلا حاجة ل curl)
# ============================================

async def send_request(host: str, port: int, command: str, payload: dict) -> dict:
    """
    An async client simulator that opens a connection, sends a request,
    waits for the response, and returns it as a dictionary.
    """
    reader, writer = await asyncio.open_connection(host, port)
    
    req_json = json.dumps({"command": command, "payload": payload}).encode('utf-8')
    writer.write(req_json)
    await writer.drain()
    
    resp_data = await reader.read(4096)
    writer.close()
    await writer.wait_closed()
    
    return json.loads(resp_data.decode('utf-8'))


# ============================================
# TESTS (unittest style)
# ============================================

class TestRequestParser(unittest.TestCase):
    """Unit tests for request parsing, handling valid JSON, invalid JSON, and missing fields."""

    def test_parse_valid_request(self):
        raw = b'{"command": "test", "payload": {"a": 1}}'
        req = RequestParser.parse(raw, ("127.0.0.1", 1234))
        self.assertEqual(req.command, "test")
        self.assertEqual(req.payload, {"a": 1})

    def test_parse_invalid_json_raises_error(self):
        with self.assertRaises(InvalidRequestError):
            RequestParser.parse(b'invalid json', ("127.0.0.1", 1234))


class TestRouter(unittest.IsolatedAsyncioTestCase):
    """Unit tests for the router, including simple routes, dynamic routes, and 404 errors."""

    async def test_route_registration_and_dispatch(self):
        router = Router()
        
        @router.route("hello")
        async def hello(req):
            return Response.success({"msg": "hi"})
            
        req = Request(command="hello", payload={})
        resp = await router.dispatch(req)
        self.assertEqual(resp.status, "ok")
        self.assertEqual(resp.body["data"]["msg"], "hi")

    async def test_dynamic_route_extracts_params(self):
        router = Router()
        
        @router.route_dynamic("user/{id}")
        async def get_user(req):
            return Response.success({"user_id": req.params.get("id")})
            
        req = Request(command="user/42", payload={})
        resp = await router.dispatch(req)
        self.assertEqual(resp.body["data"]["user_id"], "42")

    async def test_missing_route_raises_error(self):
        router = Router()
        req = Request(command="missing", payload={})
        with self.assertRaises(RouteNotFoundError):
            await router.dispatch(req)


class TestMiddleware(unittest.IsolatedAsyncioTestCase):
    """Unit tests for middleware execution order and logic."""

    async def test_middleware_execution_order(self):
        manager = MiddlewareManager()
        execution_order = []
        
        class TestMW1(Middleware):
            async def before_request(self, req):
                execution_order.append("mw1_before")
                return req
            async def after_request(self, req, res):
                execution_order.append("mw1_after")
                return res
                
        class TestMW2(Middleware):
            async def before_request(self, req):
                execution_order.append("mw2_before")
                return req
            async def after_request(self, req, res):
                execution_order.append("mw2_after")
                return res

        manager.add(TestMW1())
        manager.add(TestMW2())
        
        req = Request(command="test", payload={})
        res = Response.success({})
        
        await manager.run_before(req)
        await manager.run_after(req, res)
        
        self.assertEqual(execution_order, ["mw1_before", "mw2_before", "mw2_after", "mw1_after"])

    async def test_auth_middleware_rejects_invalid_token(self):
        mw = AuthMiddleware(valid_tokens={"secret"})
        req = Request(command="test", payload={"token": "bad"})
        with self.assertRaises(MiddlewareError):
            await mw.before_request(req)


# ============================================
# APPLICATION EXAMPLE (main.py)
# ============================================

def create_app() -> TaskQueueServer:
    """
    Factory function that builds and returns a fully configured TaskQueueServer instance,
    with registered middleware and defined routes.
    """
    app = TaskQueueServer("127.0.0.1", 8080)
    
    # Register Middlewares
    app.use_middleware(TimingMiddleware())
    app.use_middleware(LoggingMiddleware())
    
    # Register Error Handler
    @app.error_handler(RouteNotFoundError)
    async def handle_not_found(e: Exception, req: Request) -> Response:
        return Response.error("Command not found!", 404)

    # Register Static Routes
    @app.route("create_task")
    async def create_task(request: Request) -> Response:
        name = request.payload.get("name", "Unknown")
        return Response.success({"task_id": 1, "name": name, "status": "created"})

    @app.route("list_tasks")
    async def list_tasks(request: Request) -> Response:
        return Response.success({"tasks": [1, 2, 3]})
        
    # Register Dynamic Route
    @app.route_dynamic("task/{task_id}/status")
    async def get_task_status(request: Request) -> Response:
        task_id = request.params.get("task_id")
        return Response.success({"task_id": task_id, "status": "running"})

    return app


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        # Run tests if the argument "test" is provided
        sys.argv.pop()
        unittest.main()
    else:
        # Otherwise run the server
        app = create_app()
        app.run()