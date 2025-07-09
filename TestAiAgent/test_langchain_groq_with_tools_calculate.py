import json
from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain.tools import tool

# 載入 .env 檔案中的 GROQ_API_KEY
load_dotenv()

# 定義 LLM
llm = ChatGroq(model="llama-3.3-70b-versatile")

# 定義輸出格式
class CalculatorResponse(BaseModel):
    result: float

# 工具 function：加上 @tool 裝飾器，讓 LangChain 可識別
@tool
def calculate(expression: str) -> str:
    """Evaluate a mathematical expression like '2 + 2 * 10'."""
    try:
        result = eval(expression)
        return json.dumps({"result": result})
    except Exception:
        return json.dumps({"error": "Invalid expression"})

# 建立 Output Parser（這裡不強制解析格式，除非你要結構化）
parser = PydanticOutputParser(pydantic_object=CalculatorResponse)

# 建立提示模版（LangChain 標準格式）
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
            You are a calculator assistant. Answer only after using the provided 'calculate' tool. 
            Wrap your response in JSON. Avoid any explanations.\n{format_instructions}
            """,
        ),
        ("placeholder", "{chat_history}"),
        ("human", "{query}"),
        ("placeholder", "{agent_scratchpad}"),
    ]
).partial(format_instructions=parser.get_format_instructions())

# 建立 Agent
tools = [calculate]
agent = create_tool_calling_agent(llm=llm, prompt=prompt, tools=tools)

# 建立 Agent 執行器
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# 使用者輸入查詢
query = input("Enter a math expression: ")

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
