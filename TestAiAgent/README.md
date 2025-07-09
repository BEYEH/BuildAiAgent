<!-- omit in toc -->
# Test - AI Agent

<!-- omit in toc -->
## Table of contents

- [Note](#note)
- [Pathway](#pathway)
- [Resources](#resources)

## Note

## Pathway

- Setup / Requirements

  - Virtual env.

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
    pip freeze > requirements.txt
    # Upgrade pip.
    python3 -m pip install --upgrade pip
    ```

- Basic code - Setup / Imports
  - Choose a model to use.
  - Get you API key.
  - Basic LLM functionality.
- Structured - Output / Models
  - Define a simple python class which will specify the type of content that we want out LLM to generate.
- Prompt templetes
- Create & Run the agent.
  - Use `AgentExecutor` to run the agent.
    - Enable verbose mode to view the agent's reasoning process.

## Resources

- YouTube
  - [Build an AI Agent From Scratch in Python - Tutorial for Beginners](https://www.youtube.com/watch?v=bTMPwUgLZf0)
- GitHub
  - [techwithtim / PythonAIAgentFromScratch](http://github.com/techwithtim/PythonAIAgentFromScratch)
- Groq
  - [Groq API Keys](https://console.groq.com/keys)
  - [Groq Quickstart](https://console.groq.com/docs/quickstart)
- OpenAI Platform
- LangChain
  - [LangChain Python API Reference](https://python.langchain.com/api_reference/index.html)
    - [ChatPromptTemplate](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.chat.ChatPromptTemplate.html)
