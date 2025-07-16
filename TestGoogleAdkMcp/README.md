<!-- omit in toc -->
# Test - Google ADK MCP

<!-- omit in toc -->
## Table of contents

- [Target](#target)
- [App Screenshots](#app-screenshots)
- [Pathway](#pathway)
- [Steps](#steps)
- [Note](#note)
- [Resources](#resources)

## Target

## App Screenshots

## Pathway

- Using MCP servers with ADK agents (ADK as an MCP client) in `adk web`.
  - Example 01 : File System MCP Server
  - Example 02 : Google Maps MCP Server
- Building an MCP server with ADK tools (MCP server exposing ADK)¶

## Steps

- Setup env & install ADK.

  ```bash
  mkdir TestGoogleAdkMcp
  cd TestGoogleAdkMcp
  touch requirements.txt
  python -m venv .venv
  source .venv/bin/activate
  pip list
  pip install -r ./requirements.txt
  pip freeze > requirements_freeze.txt
  ```

## Note

- **Model Context Protocol (MCP)** is an open standard designed to standardize how Large Language Models (LLMs) like Gemini and Claude communicate with external applications, data sources, and tools.
- **MCP** follows a client-server architecture, defining how **data**, **templates**, and **functions** are exposed by an MCP server and consumed by an MCP client.
  - data : resources
  - templates : primpts
  - functions : tools
  - MCP client : LLM host app, AI agent

## Resources

- Google ADK
  - [Get Started](https://google.github.io/adk-docs/get-started/)
  - [Model Context Protocol (MCP)](https://google.github.io/adk-docs/mcp/)
  - [Model Context Protocol Tools](https://google.github.io/adk-docs/tools/mcp-tools/)
- Google AI for Developers
  - [All models](https://ai.google.dev/gemini-api/docs/models)
- Google AI Studio
  - [API Keys](https://aistudio.google.com/app/apikey)
