import json
from langchain_community.tools import WikipediaQueryRun, DuckDuckGoSearchRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.tools import Tool, tool
from datetime import datetime


# 工具 function：加上 @tool 裝飾器，讓 LangChain 可識別
@tool
def t_calculate(expression: str) -> str:
    """Evaluate a mathematical expression like '2 + 2 * 10'."""
    try:
        result = eval(expression)
        return json.dumps({"result": result})
    except Exception:
        return json.dumps({"error": "Invalid expression"})


@tool
def t_save_text_to_file(data: str) -> str:
    """Save text data to a local file with timestamp."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted_text = f"--- Research Output ---\nTimestamp: {timestamp}\n\n{data}\n\n"

    filename = "research_output.txt"
    with open(filename, "a", encoding="utf-8") as f:
        f.write(formatted_text)

    return f"Data successfully saved to {filename}"


duckduckgo_search = DuckDuckGoSearchRun()


@tool
def t_ddk_search(query: str) -> str:
    """Search the web using DuckDuckGo and return relevant information."""
    return duckduckgo_search.run(query)


api_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=100)
wiki_query = WikipediaQueryRun(api_wrapper=api_wrapper)


@tool
def t_wiki_search(query: str) -> str:
    """Search Wikipedia for a concise summary of the given topic."""
    return wiki_query.run(query)
