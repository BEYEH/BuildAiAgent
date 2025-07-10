from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain.agents import create_tool_calling_agent, AgentExecutor
from tools import t_calculate, t_save_text_to_file, t_ddk_search, t_wiki_search

# 載入 .env 檔案中的 GROQ_API_KEY
load_dotenv()

# 定義 LLM
llm = ChatGroq(model="llama-3.3-70b-versatile")


# 定義輸出格式
class ResearchResponse(BaseModel):
    topic: str
    tools_used: list[str]
    summary: str
    sources: list[str]


# 建立 Output Parser（這裡不強制解析格式，除非你要結構化）
parser = PydanticOutputParser(pydantic_object=ResearchResponse)

# 建立提示模版（LangChain 標準格式）
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

# 建立 Agent
tools = [t_save_text_to_file, t_wiki_search]
agent = create_tool_calling_agent(llm=llm, prompt=prompt, tools=tools)

# 建立 Agent 執行器
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# 使用者輸入查詢
query = input("User Input: ")

# 呼叫 agent_executor 執行
raw_response = agent_executor.invoke({"query": query})
print("Raw output from agent:\n", raw_response)

# 嘗試用 PydanticOutputParser 做解析（可選）
try:
    structured_response = parser.parse(raw_response.get("output"))
    print("Parsed result:\n", structured_response)
except Exception as e:
    print("❌ Error parsing response:", e)
    print("Raw Output:\n", raw_response)
