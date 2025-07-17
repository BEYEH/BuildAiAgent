<!-- omit in toc -->
# Build AI Agent

<!-- omit in toc -->
## Table of contents

- [Dev Env](#dev-env)
- [Note](#note)
- [Pathway](#pathway)
- [Resources](#resources)
- [Appendix](#appendix)

## Dev Env

- Ubuntu 22.04 LTS
- Python 3.10.12
- Virtual Env

## Note

- LangChain
  - It is a framework for building LLM-powered applications. It helps you chain together interoperable components and third-party integrations to simplify AI application development — all while future-proofing decisions as the underlying technology evolves.
- LangChain MCP Adapters
  - It is a package that makes it easy to use Anthropic Model Context Protocol (MCP) tools with LangChain & LangGraph.
- Groq
  - Groq is a company that develops ultra-fast AI inference hardware (LPU) and a cloud-based inference platform. It also offers a developer platform that allows you to use popular large language models (LLMs) like GPT-4o, LLaMA, and Gemma for free—with extremely high speed and ultra-low latency.
- LLMs
  - OpenAI - ChatGPT
  - Anthropic - Claude
  - Meta - Llama
  - Google - Gemini

## Pathway

- Basic agent
- Tools
- LiteLLM
- Structured Outputs
- Sessions & Memory
- Persistent Storage
- Multi-Agent
- Stateful Multi-Agent
- Callbacks
- Sequential Agents
- Parallel Agents
- Loop Agents

## Resources

- GitHub
  - [langchain-ai / langchain](https://github.com/langchain-ai)
- Google ADK
  - [Home](https://google.github.io/adk-docs/)
  - [Get Started](https://google.github.io/adk-docs/get-started/)
  - [Model Context Protocol (MCP)](https://google.github.io/adk-docs/mcp/)
  - [Model Context Protocol Tools](https://google.github.io/adk-docs/tools/mcp-tools/)
- Google AI for Developers
  - [All models](https://ai.google.dev/gemini-api/docs/models)
- Google AI Studio
  - [API Keys](https://aistudio.google.com/app/apikey)
- LangChain
  - [Introduction](https://python.langchain.com/docs/introduction)
- MCP
  - [Home](https://modelcontextprotocol.io/)
- Smithery
  - [Home](https://smithery.ai/)
- Ollama
  - [Ollama Library](https://ollama.com/library)
- YouTube
  - [Python Virtual Environments - Full Tutorial for Beginners](https://www.youtube.com/watch?v=Y21OR1OPC9A)
  - [Build an AI Agent From Scratch in Python - Tutorial for Beginners](https://www.youtube.com/watch?v=bTMPwUgLZf0)
  - [How to Build a Local AI Agent With Python (Ollama, LangChain & RAG)](https://www.youtube.com/watch?v=E4l91XKQSgw)
  - [MCP Crash Course for Python Developers](https://www.youtube.com/watch?v=5xqFjh56AwM)
  
## Appendix

- Virtual env.

  ``` bash
  # Create virtual env.
  sudo apt-get install python3-venv
  python3 -m venv .venv
  # Enter virtual env.
  source .venv/bin/activate
  # Exit virtual env.
  deactivate
  # Check packages.
  pip list
  # Install packages from a file.
  pip install -r ./requirements.txt
  # Saving packages.
  pip freeze > requirements.txt
  # Upgrade pip.
  python3 -m pip install --upgrade pip
  ```
