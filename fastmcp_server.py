"""
Sample FastMCP Server Application
This is a basic example to get you started with FastMCP.
Run with: python app.py
"""

from fastmcp import FastMCP
from tavily_client import search_with_tavily


# Create a server instance
server = FastMCP("remote-mcp-http-server")

@server.tool
def tavily_search(query: str) -> str:
    """
    Search the web for information.
    
    Args:
        query: The search query
        
    Returns:
        Search results
    """
    answer = search_with_tavily(query)
    return f"Search results for {query}: {answer}"

@server.tool
def greet(name: str) -> str:
    """
    Greet someone by name.
    
    Args:
        name: The name of the person to greet
        
    Returns:
        A greeting message
    """
    return f"Hello, {name}! Welcome to FastMCP."


@server.tool
def add(a: int, b: int) -> int:
    """
    Add two numbers together.
    
    Args:
        a: First number
        b: Second number
        
    Returns:
        The sum of a and b
    """
    return a + b


@server.tool
def multiply(x: float, y: float) -> float:
    """
    Multiply two numbers.
    
    Args:
        x: First number
        y: Second number
        
    Returns:
        The product of x and y
    """
    return x * y


@server.tool
def get_info() -> dict:
    """
    Get information about the server.
    
    Returns:
        Server information dictionary
    """
    return {
        "server_name": "remote-mcp-http-server",
        "version": "1.0.0",
        "status": "running",
        "available_tools": ["greet", "add", "multiply", "get_info"]
    }


if __name__ == "__main__":
    print("=" * 50)
    print("Starting FastMCP Server in HTTP Mode")
    print("=" * 50)
    print("Server running at: http://localhost:8000")
    print("API Docs at: http://localhost:8000/docs")
    print("=" * 50)
    
    # Run the FastMCP server with HTTP transport
    try:
        # Try running with HTTP transport
        server.run(transport="http", port=8000)
    except TypeError:
        # Fallback: try with different method
        try:
            server.run(mode="http", port=8000)
        except TypeError:
            print("Error: Could not start HTTP server")
            print("Running in default stdio mode...")
            server.run()
