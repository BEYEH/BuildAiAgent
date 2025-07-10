<!-- omit in toc -->
# My AI Agent

<!-- omit in toc -->
## Table of contents

- [AI Agent Tools](#ai-agent-tools)
- [Steps](#steps)
- [Resources](#resources)
- [Appendix](#appendix)

## AI Agent Tools

- DuckDuckGoSearchRun

## Steps

- Setup / Requirements
- Use LLM.
  - Load API key.
  - Choose model.
- Use agnet.
  - Structured output.
  - Prompt templetes.
  - Create `AgentExecutor`.
- Output parsing.
- Add tools.

## Resources

- LangChain
  - [Components](https://python.langchain.com/docs/integrations/components/)
    - [ChatGroq](https://python.langchain.com/docs/integrations/chat/groq/)
  - [Doc](https://python.langchain.com/docs/introduction)
  - [Python API Reference](https://python.langchain.com/api_reference/index.html)
    - [DuckDuckGoSearchRun](https://python.langchain.com/api_reference/community/tools/langchain_community.tools.ddg_search.tool.DuckDuckGoSearchRun.html)
  - [ChatPromptTemplate](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.chat.ChatPromptTemplate.html)
- Groq Cloud
  - [API Keys](https://console.groq.com/keys)
- Others
  - [DuckDuckGo](https://duckduckgo.com/)

## Appendix

- Create virtial env & install packages.

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
