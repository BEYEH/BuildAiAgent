import asyncio
from mcp import ClientSession
from mcp.client.sse import sse_client


async def main():
    url = "http://127.0.0.1:8050/sse"
    toolcalling = "say_hello"

    # Connect to the server using SSE
    async with sse_client(url=url) as (read_stream, write_stream):
        async with ClientSession(read_stream, write_stream) as session:
            # Initialize the connection
            await session.initialize()

            # List available tools
            tools_result = await session.list_tools()
            print("Available tools:")
            for tool in tools_result.tools:
                print(f"  - {tool.name}: {tool.description}")

            # Call tool
            result = await session.call_tool(
                name=toolcalling, arguments={"name": "John"}
            )
            print(f"{result.content[0].text}")


if __name__ == "__main__":
    asyncio.run(main())
