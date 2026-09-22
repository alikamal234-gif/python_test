class Request:
    def __init__(self, method, path, header, body, query_params=None):
        self.method = method
        self.path = path
        self.header = header
        self.body = body

        if query_params is None:
            query_params = {}

        self.query_params = query_params
        self.path_params = {}


class Parser:
    def __init__(self, request):
        self.request = request

    def convert(self):

        lines = self.request.splitlines()

        request_line = lines[0]

        method = request_line.split()[0]

        target = request_line.split()[1]

        path = target.split("?", 1)[0]

        query_params = {}

        if "?" in target:

            query_string = target.split("?", 1)[1]

            query_params_string = query_string.split("&")

            for query in query_params_string:

                key, value = query.split("=", 1)

                query_params[key] = value

        header = {}

        body = ""

        body_index = None

        for i in range(1, len(lines)):

            if lines[i].strip() == "":
                body_index = i + 1
                break

            key, value = lines[i].split(":", 1)

            header[key] = value.strip()

        if body_index is not None:
            body = "\n".join(lines[body_index:])

        request = Request(
            method,
            path,
            header,
            body,
            query_params
        )

        return request

raw_request = """POST /users/42?active=true&role=admin HTTP/1.1
Host: localhost:8000
Content-Type: application/json
Content-Length: 23
User-Agent: Mozilla/5.0
Accept: application/json
Connection: keep-alive

{"name":"Ali","age":20}"""

parser = Parser(raw_request)
request = parser.convert()
print(request.method)
print(request.path)
print(request.query_params)
print(request.header)
print(request.body)