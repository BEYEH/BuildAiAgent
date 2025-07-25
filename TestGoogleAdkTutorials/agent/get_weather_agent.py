from google.adk.agents import Agent

from tool import get_weather


def get_weather_agent(model):
    print("weather_agent")

    weather_agent = Agent(
        name="weather_agent_v1",
        model=model,  # Can be a string for Gemini or a LiteLlm object
        description="Provides weather information for specific cities.",
        instruction="You are a helpful weather assistant. "
        "When the user asks for the weather in a specific city, "
        "use the 'get_weather' tool to find the information. "
        "If the tool returns an error, inform the user politely. "
        "If the tool is successful, present the weather report clearly.",
        tools=[get_weather],  # Pass the function directly
    )

    print(f"Agent '{weather_agent.name}' created using model '{model}'.")

    return weather_agent
