from mcp.server.fastmcp import FastMCP

mcp = FastMCP("MyServer", host="127.0.0.1", port=8050)


@mcp.tool()
def say_hello(name: str) -> str:
    """Say hello to someone

    Args:
        name: The person's name to greet
    """
    return f"Hello, {name}! Nice to meet you."


if __name__ == "__main__":
    mcp.run()
