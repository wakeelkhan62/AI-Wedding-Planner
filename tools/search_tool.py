from typing import Dict, Any

from tavily import TavilyClient
from langchain.tools import tool

tavily_client = TavilyClient()


@tool
def web_search(query: str) -> Dict[str, Any]:
    """
    Search the web for up-to-date information.

    Use this tool whenever you need information
    about venues, hotels, restaurants,
    wedding services or any real-world data.
    """

    try:
        result = tavily_client.search(
            query=query,
            max_results=5
        )

        return result

    except Exception as e:
        return {
            "error": str(e)
        }