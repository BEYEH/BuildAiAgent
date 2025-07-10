<!-- omit in toc -->
# Build AI Agent

<!-- omit in toc -->
## Table of contents

- [Dev Env](#dev-env)
- [Note](#note)
- [Pathway](#pathway)
- [Resources](#resources)

## Dev Env

- Ubuntu 22.04 LTS
- Python 3.10.12

## Note

- LangChain
  - It is a framework for building LLM-powered applications. It helps you chain together interoperable components and third-party integrations to simplify AI application development — all while future-proofing decisions as the underlying technology evolves.
- Groq
  - Groq is a company that develops ultra-fast AI inference hardware (LPU) and a cloud-based inference platform. It also offers a developer platform that allows you to use popular large language models (LLMs) like GPT-4o, LLaMA, and Gemma for free—with extremely high speed and ultra-low latency.
- LLMs
  - OpenAI - ChatGPT
  - Anthropic - Claude
  - Meta - Llama
  - Google - Gemini

## Pathway

- Virtual env.

  ``` bash
  # Create virtual env.
  sudo apt-get install python3-venv
  python3 -m venv venv
  # Enter virtual env.
  source venv/bin/activate
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

## Resources

- GitHub
  - [langchain-ai / langchain](https://github.com/langchain-ai)
- YouTube
  - [Python Virtual Environments - Full Tutorial for Beginners](https://www.youtube.com/watch?v=Y21OR1OPC9A)
  - [Build an AI Agent From Scratch in Python - Tutorial for Beginners](https://www.youtube.com/watch?v=bTMPwUgLZf0)
  - [How to Build a Local AI Agent With Python (Ollama, LangChain & RAG)](https://www.youtube.com/watch?v=E4l91XKQSgw)
- Google ADK
  - [Home](https://google.github.io/adk-docs/)
- MCP
  - [Home](https://modelcontextprotocol.io/)
- Smithery
  - [Home](https://smithery.ai/)
