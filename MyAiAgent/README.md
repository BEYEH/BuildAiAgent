<!-- omit in toc -->
# My AI Agent

<!-- omit in toc -->
## Table of contents

- [Tools](#tools)
- [Steps](#steps)
- [Resources](#resources)

## Tools

## Steps

- Setup / Requirements

  ```bash
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
  pip freeze > requirements_freeze.txt
  # Upgrade pip.
  python3 -m pip install --upgrade pip
  ```

## Resources

- LangChain
  - [Components](https://python.langchain.com/docs/integrations/components/)
    - [ChatGroq](https://python.langchain.com/docs/integrations/chat/groq/)
  - [Doc](https://python.langchain.com/docs/introduction)
  - [Python API Reference](https://python.langchain.com/api_reference/index.html)
  - [ChatPromptTemplate](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.chat.ChatPromptTemplate.html)
- Groq Cloud
  - [API Keys](https://console.groq.com/keys)
