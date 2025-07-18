import asyncio

from dotenv import load_dotenv
from langchain_mcp_adapters.tools import load_mcp_tools
from langchain_groq import ChatGroq
from langgraph.prebuilt import create_react_agent
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

load_dotenv()


async def main():
    model = ChatGroq(model="llama-3.3-70b-versatile")

    server_params = StdioServerParameters(
        command="python",
        args=["server.py"],
    )

    # Connect to the server
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            # Initialize the connection
            await session.initialize()

            # Get tools
            tools = await load_mcp_tools(session)

            # Create and run the agent
            agent = create_react_agent(model, tools)

            query = input("User Input: ")

            agent_response = await agent.ainvoke({"messages": query})
            print(f"Response: {agent_response}")
            tool_message = agent_response["messages"][2]
            print(f"Tool result: {tool_message.content}")
            ai_message = agent_response["messages"][3]
            print(f"AIMessage: {ai_message.content}")


if __name__ == "__main__":
    asyncio.run(main())
