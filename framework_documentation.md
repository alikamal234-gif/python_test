# 🚀 Python Framework Concepts Documentation

This document explains all the fundamental Python concepts used in `mini_projet.py` and provides a complete reference with examples for every class and method.

---

## 🏗️ 1. Object-Oriented Programming (OOP)

OOP is a programming paradigm based on the concept of "objects", which contain data and code. 

- **Classes (`class`)**: A blueprint for creating objects. Think of a class as a mold, and objects as the items made from that mold. For example, `class Router:` defines how a router should behave.
- **Methods**: Functions that belong to a class (e.g., `def dispatch(self, request):`). The first parameter is almost always `self`, which refers to the specific object calling the method.
- **Inheritance**: Creating a new class from an existing one to share its behavior. For example, `class RouteNotFoundError(Exception):` means `RouteNotFoundError` is a specialized version of the built-in `Exception` class. `class LoggingMiddleware(Middleware):` inherits the structure of the base `Middleware` class.

---

## ✨ 2. Magic Methods (Dunder Methods)

Magic methods in Python start and end with double underscores (`__`). They are called automatically by Python in specific situations.

### `__init__(self)`
This is the **constructor** method. It is called automatically whenever you create a new object from a class. It is used to initialize the object's attributes.

**Example from code:**
```python
class Router:
    def __init__(self):
        # This code runs automatically when you do: my_router = Router()
        self._routes = {}
        self._dynamic_routes = []
```

---

## 🎁 3. Decorators (`@`)

Decorators are a powerful way to modify or extend the behavior of a function or class without permanently modifying its actual source code. They are written above a function/class starting with the `@` symbol.

### Built-in Python Decorators:
- **`@dataclass`**: Automatically generates boilerplate code like `__init__`, `__repr__`, etc. for classes that primarily just store data (like our `Request` and `Response` objects).
- **`@classmethod`**: A method bound to the class itself, not the object of the class. It takes `cls` (the class) as the first parameter instead of `self`. Useful for factory methods (like `Response.success()`).
- **`@staticmethod`**: A method that belongs to a class but doesn't have access to `self` or `cls`. It's just a normal function put inside a class for organizational purposes (like `RequestParser.parse()`).

### `functools.wraps` (`@wraps(func)`)
When you create a custom decorator, the original function's name and documentation are usually lost. `@wraps` copies the metadata of the original function to the new wrapper function so it maintains its original identity.

### Custom Decorators (e.g., `@app.route()`, `@error_handler()`)
These are functions that take another function as an argument and extend its behavior. In our framework, they are used to "register" functions to specific tasks or routes.

---

## ⚡ 4. Asynchronous Programming (`async def` / `await`)

Normal Python code is synchronous (it executes line 1, waits for it to finish, then executes line 2). Asynchronous programming allows Python to handle multiple things concurrently, which is incredibly useful for networking (like our TCP server) where you spend a lot of time waiting for data.

- **`async def`**: Defines a "coroutine", which is a function that can be paused and resumed.
- **`await`**: Used inside an `async def` function. It tells Python to "pause execution here and wait for this operation to finish; meanwhile, go do other useful work."

---

## 📚 5. Complete API Reference with Examples

Here is a breakdown of every component in the file and how to use it.

### Exceptions
Custom errors used to signal specific problems in the framework.
- `RouteNotFoundError`: Raised when a client asks for a command that hasn't been registered.
- `InvalidRequestError`: Raised when the client sends malformed JSON.
- `MiddlewareError`: Raised when a request is blocked intentionally (e.g., bad auth token).

### Data Models

#### `Request`
Represents an incoming message from a client.
```python
# Example Usage:
req = Request(command="ping", payload={"msg": "hello"}, client_addr=("127.0.0.1", 5000))

# Safely extract data from payload
message = req.get("msg", "default_value") # Returns "hello"
```

#### `Response`
Represents the message we send back to the client.
```python
# Example Usage:
success_resp = Response.success({"status": "created", "id": 5})
error_resp = Response.error("Item not found", 404)

# Framework uses this internally to send data back over TCP
json_string = success_resp.to_json() 
```

### Parsing

#### `RequestParser`
Takes raw bytes from the network and turns them into a Python `Request` object.
```python
# Example Usage:
raw_bytes = b'{"command": "hello", "payload": {"name": "Ali"}}'
req = RequestParser.parse(raw_bytes, ("127.0.0.1", 5000))
```

### Routing

#### `Router`
Manages tying commands (strings) to their handler functions.
- `route(command)`: Decorator for exact string matches.
- `route_dynamic(pattern)`: Decorator for matches with variables (like IDs).
- `dispatch(request)`: Finds and runs the correct handler for an incoming request.

```python
router = Router()

# Exact match route
@router.route("ping")
async def ping(req: Request) -> Response:
    return Response.success({"msg": "pong"})

# Dynamic route extracting ID
@router.route_dynamic("user/{id}")
async def get_user(req: Request) -> Response:
    user_id = req.params.get("id")
    return Response.success({"user": user_id})

# Internal usage example:
# response = await router.dispatch(Request(command="user/123", payload={}))
```

### Middleware System
Middlewares act like a tunnel. They intercept requests before they reach the router, and intercept responses before they are sent back to the client.

#### `Middleware` (Base Class)
You create custom middlewares by inheriting from this class.
```python
class MyCustomMiddleware(Middleware):
    async def before_request(self, req: Request) -> Request:
        print(f"Incoming command: {req.command}")
        return req # Must return the request!
        
    async def after_request(self, req: Request, res: Response) -> Response:
        res.body["intercepted_by"] = "MyCustomMiddleware"
        return res # Must return the response!
```

#### Pre-built Middlewares
- `LoggingMiddleware`: Automatically prints details of requests and responses.
- `TimingMiddleware`: Measures and logs how long a request took to process.
- `AuthMiddleware`: Requires a valid token in the payload to proceed.

#### `MiddlewareManager`
Manages the list of middlewares and runs them in the correct order.
```python
manager = MiddlewareManager()
manager.add(LoggingMiddleware())
manager.add(AuthMiddleware(valid_tokens={"secret123"}))
```

### Error Handling

#### `ErrorHandlerRegistry` and `@error_handler`
Allows you to register custom functions to handle specific exceptions gracefully, preventing the server from crashing.
```python
registry = ErrorHandlerRegistry()

# Register a custom handler for InvalidRequestError
@error_handler(InvalidRequestError)
async def handle_bad_json(e: Exception, req: Request) -> Response:
    return Response.error("Bad JSON format! Please check your syntax.", 400)

registry.register(InvalidRequestError, handle_bad_json)
```

### Server and Client Setup

#### `TaskQueueServer`
The main application class that brings everything together (Router, Middleware, Errors, TCP server).
```python
app = TaskQueueServer("127.0.0.1", 8080)

# Add Middlewares
app.use_middleware(LoggingMiddleware())

# Define Routes
@app.route("test")
async def test(req: Request) -> Response:
    return Response.success({"ok": True})

# Start the server (runs forever)
# app.run() 
```

#### `send_request`
A helper function to test your server from another Python script without needing external tools like `curl`.
```python
# Client side script to test the server:
import asyncio

async def main():
    response = await send_request("127.0.0.1", 8080, "test", {})
    print(response)

# asyncio.run(main())
```
