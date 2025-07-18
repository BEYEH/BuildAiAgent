from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Math")


@mcp.tool()
def plus(a: int, b: int) -> int:
    """Plus two numbers"""
    return a + b


@mcp.tool()
def minus(a: int, b: int) -> int:
    """Minus two numbers"""
    return a - b


@mcp.tool()
def multiplied(a: int, b: int) -> int:
    """Multiplied two numbers"""
    return a * b


@mcp.tool()
def divided(a: int, b: int) -> int:
    """Divided two numbers"""
    return a / b


if __name__ == "__main__":
    mcp.run(transport="stdio")
