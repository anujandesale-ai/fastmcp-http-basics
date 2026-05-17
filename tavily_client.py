"""
Tavily Client Integration
Uses Tavily API for web search functionality
"""

import os
from dotenv import load_dotenv
from tavily import TavilyClient

# Load environment variables from .env file
load_dotenv()

# Get API key from environment
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

if not TAVILY_API_KEY:
    raise ValueError("TAVILY_API_KEY not found in .env file")

# Initialize Tavily client
tavily_client = TavilyClient(api_key=TAVILY_API_KEY)

# Example: Search with Tavily
def search_with_tavily(query: str):
    """Search using Tavily API"""
    print(f"\nSearching for: {query}")
    try:
        response = tavily_client.search(query=query, max_results=5)
        print(f"Found {len(response['results'])} results:")
        for i, result in enumerate(response['results'], 1):
            print(f"\n{i}. {result['title']}")
            print(f"   URL: {result['url']}")
            print(f"   Content: {result['content'][:150]}...")
        return response
    except Exception as e:
        print(f"Error: {e}")
        return None

# Test
if __name__ == "__main__":
    print("=" * 50)
    print("Tavily Client Test")
    print("=" * 50)
    
    # Example search
    results = search_with_tavily("FastMCP Python")
    
    print("\n" + "=" * 50)
    print("Full Response:")
    print(results)
