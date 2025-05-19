from fastmcp import FastMCP
from dotenv import load_dotenv
import json
import os
import requests
from bs4 import BeautifulSoup

load_dotenv()

mcp = FastMCP("My MCP Server")

USER_AGENT = "docs-app/1.0"
SERPER_URL = "https://google.serper.dev/search"

docs_urls = {
    "langchain": "https://python.langchain.com/docs/",
    "llama-index": "https://docs.llamaindex.ai/en/stable/",
    "openai": "https://platform.openai.com/docs"
}

async def search_web(query: str) -> dict | None:
    payload = json.dumps({
        "q": query
    })
    headers = {
        'X-API-KEY': os.getenv("SERPER_API_KEY"),
        'Content-Type': 'application/json'
    }

    response = requests.post(SERPER_URL, headers=headers, data=payload)
    
    if response.status_code != 200:
        print(f"Error: {response.status_code} - {response.text}")
        return None
    
    return response.json()

async def fetch_url(url: str):
    try:
        response = requests.get(url, headers={"User-Agent": USER_AGENT})
        soup = BeautifulSoup(response.text, "html.parser")
        text = soup.get_text()
        return text
    except Exception as e:
        raise e

@mcp.tool()
async def get_docs(query: str, library: str):
    """
    Search the latest docs for a given query and library.
    Supports langchain, openai, and llama-index.

    Args:
        query: The query to search for (e.g. "Chroma DB")
        library: The library to search in (e.g. "langchain")

    Returns:
        Text from the docs
    """

    if library not in docs_urls:
        raise ValueError(f"Library {library} not supported by this tool")
   
    full_query = f"site:{docs_urls[library]} {query}"
    results = await search_web(full_query)

    if not results or not results.get("organic"):
        return "No results found."

    text = ""
    for result in results["organic"][:3]: 
        text += await fetch_url(result["link"])

    return text

if __name__ == "__main__":
    mcp.run(transport="stdio")
