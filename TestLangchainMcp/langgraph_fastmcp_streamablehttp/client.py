import asyncio

from dotenv import load_dotenv
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

from langchain_groq import ChatGroq
from langchain_mcp_adapters.tools import load_mcp_tools
from langgraph.prebuilt import create_react_agent

load_dotenv()


async def main():
    model = ChatGroq(model="llama-3.3-70b-versatile")

    server_params = StdioServerParameters(
        command="python",
        args=["server.py"],
    )

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            # Initialize the connection
            await session.initialize()

            # Get tools
            tools = await load_mcp_tools(session)

            # Create and run the agent
            agent = create_react_agent(model, tools)
            agent_response = await agent.ainvoke(
                {
                    "messages": "Please calculate (3 + 5) x 12 step by step. First add 3 and 5, then multiply the result by 12."
                }
            )
            ai_message = agent_response["messages"][3]
            print(f"AIMessage: {ai_message.content}")


if __name__ == "__main__":
    asyncio.run(main())
