from dotenv import load_dotenv
from langchain_groq import ChatGroq
from pydantic import BaseModel
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain.agents import create_tool_calling_agent, AgentExecutor
from tools.ddg_search_tool import t_ddg_search
from tools.save_text_tool import t_save_text_to_file
from tools.wiki_search_tool import t_wiki_search

load_dotenv()


class ResearchResponse(BaseModel):
    topic: str
    tools_used: list[str]
    summary: str
    sources: list[str]


def main():
    llm = ChatGroq(model="llama-3.3-70b-versatile")
    tools = [t_ddg_search, t_wiki_search, t_save_text_to_file]

    query = input("User Input: ")

    parser = PydanticOutputParser(pydantic_object=ResearchResponse)
    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                """
                You are a research assistant that will help generate a research paper.
                Answer the user query and use neccessary tools. 
                Wrap the output in this format and provide no other text\n{format_instructions}
                """,
            ),
            ("placeholder", "{chat_history}"),
            ("human", "{query}"),
            ("placeholder", "{agent_scratchpad}"),
        ]
    ).partial(format_instructions=parser.get_format_instructions())

    agent = create_tool_calling_agent(llm=llm, prompt=prompt, tools=tools)

    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

    raw_response = agent_executor.invoke({"query": query})

    try:
        structured_response = parser.parse(raw_response.get("output"))
        print("Result:\n", structured_response)
    except Exception as e:
        print("Exception: \n", e)


if __name__ == "__main__":
    main()
