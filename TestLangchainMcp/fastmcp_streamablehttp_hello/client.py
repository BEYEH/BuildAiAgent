import asyncio
from mcp import ClientSession
from mcp.client.streamable_http import streamablehttp_client


async def main():
    url = "http://localhost:8050/mcp"
    toolcalling = "say_hello"

    # Connect to the server using SSE
    async with streamablehttp_client(url=url) as (
        read_stream,
        write_stream,
        get_session_id,
    ):
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
