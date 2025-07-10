from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.tools import tool

api_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=100)
wiki_query = WikipediaQueryRun(api_wrapper=api_wrapper)


@tool
def t_wiki_search(query: str) -> str:
    """Search Wikipedia for a concise summary of the given topic."""
    return wiki_query.run(query)
