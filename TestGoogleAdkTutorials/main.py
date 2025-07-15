import asyncio
from dotenv import load_dotenv
from google.adk.sessions import InMemorySessionService
from google.adk.runners import Runner

from lib import check_api_key, call_agent_async, run_conversation
from agent import get_weather_agent


async def main():
    """
    Constant
    """
    MODEL_GEMINI_2_0_FLASH = "gemini-2.0-flash"
    MODEL_GEMINI_2_0_FLASH_LIVE = "gemini-2.0-flash-live-001"
    MODEL = MODEL_GEMINI_2_0_FLASH
    APP_NAME = "weather_tutorial_app"
    USER_ID = "user_1"
    SESSION_ID = "session_001"

    load_dotenv()

    check_api_key()

    """
    Session Management
        Key Concept: SessionService stores conversation history & state.
        InMemorySessionService is simple, non-persistent storage for this tutorial.
    """
    session_service = InMemorySessionService()

    weather_agent = get_weather_agent(MODEL)

    session = await session_service.create_session(  #
        app_name=APP_NAME, user_id=USER_ID, session_id=SESSION_ID
    )
    print(f"會話已創建：應用程式='{APP_NAME}', 用戶='{USER_ID}', 會話='{SESSION_ID}'")

    runner = Runner(
        agent=weather_agent,  # 我們想要運行的 Agent
        app_name=APP_NAME,  # 將運行與我們的應用程式關聯
        session_service=session_service,  # 使用我們的會話管理器
    )
    print(f"Runner 已為 Agent '{runner.agent.name}' 創建。")

    await run_conversation(runner, USER_ID, SESSION_ID)


if __name__ == "__main__":
    asyncio.run(main())
