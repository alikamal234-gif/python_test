import re
class Route :
    def __init__(self , path , method , handler):
        self.path = path
        self.methods = method 
        self.handler = handler
    def match_path(self , request_path):

        route_parts = self.path.split("/")
        request_parts = request_path.split("/")

        if len(route_parts) != len(request_parts):
            return None

        params = {}

        for route_part, request_part in zip(route_parts, request_parts):

            if route_part == request_part:
                continue
            if route_part.startswith("{") and route_part.endswith("}"):
                name = route_part[1:-1]
                params[name] = request_part
                continue

            return None

        return params

class Router :
    def __init__(self):
        self.routes = []

    def add_route(self , path , method , handler):
        route = Route(path , method , handler)
        self.routes.append(route)

    def match(self, method, path):

        path_found = False
    
        for route in self.routes:
        
            params = route.match_path(path)
    
            if params is None:
                continue
            
            path_found = True
    
            if method not in route.methods:
                continue
            
            return route.handler, params
    
        if path_found:
            return "405 Method not allowed"
    
        return "404 Not found"

def home():
    return "welcome to Home"


def user(id):
    return f"User {id}"


router = Router()

router.add_route(
    "/",
    ["GET", "POST", "PUT"],
    home
)

router.add_route(
    "/users/{id}",
    ["GET"],
    user
)
router.add_route(
    "/files/{filename}",
    ["GET"],
    user
)
router.add_route(
    "/users/{id}/posts/{post_id}",
    ["GET"],
    user
)

print(router.match("GET", "/sq"))
print(router.match("PUT", "/users/42"))
print(router.match("GET", "/users/20/posts/45"))
print(router.match("GET", "/files/26"))