from langchain_community.tools import DuckDuckGoSearchRun
from langchain.tools import tool

duckduckgo_search = DuckDuckGoSearchRun()


@tool
def t_ddg_search(query: str) -> str:
    """Search the web using DuckDuckGo and return relevant information."""
    return duckduckgo_search.run(query)
