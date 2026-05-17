"""
Test Client for FastMCP Server using MCP Protocol
This script tests the running FastMCP server.
Make sure the server is running first: python app.py

Run with: python test_mcp_client.py
"""
import asyncio
from fastmcp import Client

client = Client("http://localhost:8000/mcp")

async def check_greet(name: str):
    async with client:
        result = await client.call_tool("greet", {"name": name})
        print(result)

asyncio.run(check_greet("Ford"))

async def test_add(a: int, b:int):
    """Test the add tool."""
    print("\nTest 2: Add tool")
    async with client:
        result = await client.call_tool("add", {"a": a, "b": b})
        print(result)

asyncio.run(test_add(10, 5))

async def test_list_tools():
    """List available tools."""
    print("\nTest: List Tools")
    async with client:
        tools = await client.list_tools()
        print(f"Available tools: {[tool.name for tool in tools]}")
        
asyncio.run(test_list_tools())

async def test_tavily_search(query: str):
    """Test the tavily_search tool."""
    print("\nTest: Tavily Search")
    async with client:
        result = await client.call_tool("tavily_search", {"query": query})
        print(result)

asyncio.run(test_tavily_search("What is FastMCP?"))
