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

- YouTube
  - [Python Virtual Environments - Full Tutorial for Beginners](https://www.youtube.com/watch?v=Y21OR1OPC9A)
  - [Build an AI Agent From Scratch in Python - Tutorial for Beginners](https://www.youtube.com/watch?v=bTMPwUgLZf0)
  - [How to Build a Local AI Agent With Python (Ollama, LangChain & RAG)](https://www.youtube.com/watch?v=E4l91XKQSgw)
