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
    - Take the place of SSE transport.
    - Better Performance: 3-5x improvement under high concurrency.
    - Simplified Architecture: Single endpoint instead of separate HTTP + SSE endpoints.
    - Enhanced Scalability: Better support for multi-node deployments.
    - Modern Standards: Built on current HTTP streaming standards.
    - Supports both stateful and stateless operation modes.
    - Recommended for use in production environments due to its good performance and scalability.
  - Server-Sent Events (SSE) : `sse_client`
    - For HTTP-based communication.
    - Split client and server into seperate applications.
  - Standard I/O : `stdio_client`
    - Server communications through standard input and output.
    - Client and server run in same process.
    - Client directly launches the server as a subprocess.
    - No seperate server process is needed.

## Resources

- LangChain
  - [Introduction](https://python.langchain.com/docs/introduction)
  - [MCP Adapters for LangChain and LangGraph](https://changelog.langchain.com/announcements/mcp-adapters-for-langchain-and-langgraph)
- GitHub
  - [langchain-ai / langchain-mcp-adapters](https://github.com/langchain-ai/langchain-mcp-adapters)
  - [daveebbelaar / ai-cookbook](https://github.com/daveebbelaar/ai-cookbook/tree/main)
