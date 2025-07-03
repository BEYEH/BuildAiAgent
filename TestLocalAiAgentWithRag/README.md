<!-- omit in toc -->
# Test - Local AI Agent with RAG

<!-- omit in toc -->
## Table of contents

- [Note](#note)
- [Pathway](#pathway)
- [Resources](#resources)

## Note

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

- Ollama

  ``` bash
  # Download.
  curl -fsSL https://ollama.com/install.sh | 
  # Check.
  ollama
  # Install Ollama models.
  ollama pull llama3.2
  ollama pull mxbai-embed-large
  ```

## Resources

- [Ollama](https://ollama.com/)
  - [Ollama Library](https://ollama.com/library)
- YouTube
  - [How to Build a Local AI Agent With Python (Ollama, LangChain & RAG)](https://www.youtube.com/watch?v=E4l91XKQSgw)
  - [Learn Ollama in 15 Minutes - Run LLM Models Locally for FREE](https://www.youtube.com/watch?v=UtSSMs6ObqY)
- GitHub
  - [techwithtim / LocalAIAgentWithRAG](https://github.com/techwithtim/LocalAIAgentWithRAG)
