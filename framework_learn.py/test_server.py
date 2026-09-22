import asyncio

async def handle_client(reader , writer):
    print("Client connceted")
    data = await reader.read(1024)
    print(data.decode())
    body = "server running"
    response = (
        "HTTP/1.1 200 OK\r\n"
        "Content-Type: text/plain\r\n"
        f"Content-Length: {len(body.encode())}\r\n"
        "\r\n"
        f"{body}"
    )

    writer.write(response.encode())
    await writer.drain()
    writer.close()
    await writer.wait_closed()

async def main():
    server = await asyncio.start_server(
        handle_client,
        "127.0.0.1",
        8000
    )
    print("Server running on http://127.0.0.1:8000")
    await server.serve_forever()

asyncio.run(main())