from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Math")


@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


@mcp.tool()
def multiply(a: int, b: int) -> int:
    """Multiply two numbers"""
    return a * b


@mcp.tool()
def calculate_expression(expression: str) -> str:
    """Safely evaluate a mathematical expression

    Args:
        expression: Mathematical expression like "(3 + 5) * 12"
    """
    try:
        allowed_chars = set("0123456789+-*/(). ")
        if all(c in allowed_chars for c in expression):
            result = eval(expression)
            return f"{expression} = {result}"
        else:
            return "Invalid expression"
    except:
        return "Error evaluating expression"


if __name__ == "__main__":
    mcp.run(transport="stdio")
