import asyncio
import logging
import os
import aiohttp
from fastmcp import FastMCP 

logger = logging.getLogger(__name__)
logging.basicConfig(format="[%(levelname)s]: %(message)s", level=logging.INFO)

mcp = FastMCP("MCP Server on Cloud Run")

@mcp.tool()
def add(a: int, b: int) -> int:
    """Use this to add two numbers together."""
    logger.info(f">>> Tool: 'add' called with numbers '{a}' and '{b}'")
    return a + b

@mcp.tool()
def subtract(a: int, b: int) -> int:
    """Use this to subtract two numbers."""
    logger.info(f">>> Tool: 'subtract' called with numbers '{a}' and '{b}'")
    return a - b

@mcp.tool()
async def random_joke() -> str:
    """Get a random joke from the Official Joke API.
    
    Returns:
        A random joke with setup and punchline.
    """
    logger.info(">>> Tool: 'random_joke' called")
    
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get('https://official-joke-api.appspot.com/random_joke') as response:
                if response.status == 200:
                    joke_data = await response.json()
                    return f"{joke_data['setup']}\n\n{joke_data['punchline']}"
                else:
                    return f"Error: Could not fetch joke. Status code: {response.status}"
                    
    except Exception as e:
        logger.error(f"Error fetching joke: {e}")
        return f"Error: {str(e)}"

@mcp.tool()
async def programming_joke() -> str:
    """Get a random programming-themed joke.
    
    Returns:
        A programming-related joke.
    """
    logger.info(">>> Tool: 'programming_joke' called")
    
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get('https://official-joke-api.appspot.com/jokes/programming/random') as response:
                if response.status == 200:
                    jokes = await response.json()
                    if jokes:
                        joke = jokes[0]
                        return f"{joke['setup']}\n\n{joke['punchline']}"
                    return "No programming jokes found."
                else:
                    return f"Error: Could not fetch joke. Status code: {response.status}"
                    
    except Exception as e:
        logger.error(f"Error fetching programming joke: {e}")
        return f"Error: {str(e)}"

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8080))
    logger.info(f"MCP server started on port {port}")
    
    asyncio.run(
        mcp.run_async(
            transport="sse", 
            host="0.0.0.0", 
            port=port,
        )
    )