<!-- omit in toc -->
# Test - LangChain with MCP Adapters

<!-- omit in toc -->
## Table of contents

- [Target](#target)
- [Steps](#steps)
- [Note](#note)
- [Resources](#resources)

## Target

## Steps

- Setup env & install ADK.

  ```bash
  mkdir TestLangchainMcp
  cd TestLangchainMcp
  touch requirements.txt
  python -m venv .venv
  source .venv/bin/activate
  pip list
  pip install -r ./requirements.txt
  pip freeze > requirements_freeze.txt
  ```

## Note

- Client side implementation ways:
  - Streamable HTTP : `streamablehttp_client`
  - Server-Sent Events (SSE) : `sse_client`
  - Standard I/O : `stdio_client`

## Resources

- LangChain
  - [Introduction](https://python.langchain.com/docs/introduction)
  - [MCP Adapters for LangChain and LangGraph](https://changelog.langchain.com/announcements/mcp-adapters-for-langchain-and-langgraph)
- GitHub
  - [langchain-ai / langchain-mcp-adapters](https://github.com/langchain-ai/langchain-mcp-adapters)
  - [daveebbelaar / ai-cookbook](https://github.com/daveebbelaar/ai-cookbook/tree/main)
