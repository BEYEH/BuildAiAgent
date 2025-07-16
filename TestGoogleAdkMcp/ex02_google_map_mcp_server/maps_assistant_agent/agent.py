import os
from google.adk.agents import LlmAgent
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, StdioServerParameters

google_maps_api_key = os.environ.get("GOOGLE_MAPS_API_KEY")

if not google_maps_api_key:
    google_maps_api_key = "YOUR_GOOGLE_MAPS_API_KEY_HERE"
    if google_maps_api_key == "YOUR_GOOGLE_MAPS_API_KEY_HERE":
        print(
            "WARNING: GOOGLE_MAPS_API_KEY is not set. Please set it as an environment variable or in the script."
        )

root_agent = LlmAgent(
    model="gemini-2.0-flash",
    name="maps_assistant_agent",
    instruction="Help the user with mapping, directions, and finding places using Google Maps tools.",
    tools=[
        MCPToolset(
            connection_params=StdioServerParameters(
                command="npx",
                args=[
                    "-y",
                    "@modelcontextprotocol/server-google-maps",
                ],
                # Pass the API key as an environment variable to the npx process
                # This is how the MCP server for Google Maps expects the key.
                env={"GOOGLE_MAPS_API_KEY": google_maps_api_key},
            ),
            # You can filter for specific Maps tools if needed:
            # tool_filter=['get_directions', 'find_place_by_id']
        )
    ],
)
