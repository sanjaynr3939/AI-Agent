import os

from dotenv import load_dotenv
from tavily import TavilyClient

load_dotenv("aiagent.env")

client = TavilyClient(
    api_key=os.getenv("TAVILY_API_KEY")
)

def search_web(query: str) -> str:
    """
    Search the web using Tavily.
    """

    response = client.search(
        query=query,
        max_results=3
    )

    results = response.get("results", [])

    if not results:
        return "No results found."

    output = ""

    for result in results:
        output += f"Title: {result['title']}\n"
        output += f"Content: {result['content']}\n"
        output += f"URL: {result['url']}\n\n"

    return output