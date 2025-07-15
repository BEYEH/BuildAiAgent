from dotenv import load_dotenv

from lib import check_api_key
from agent import weather_agent


def main():
    """
    Constant
    """
    MODEL_GEMINI_2_0_FLASH = "gemini-2.0-flash"
    MODEL_GEMINI_2_0_FLASH = "gemini-2.0-flash-live-001"
    MODEL = MODEL_GEMINI_2_0_FLASH

    load_dotenv()

    check_api_key()

    weather_agent(MODEL)


if __name__ == "__main__":
    main()
