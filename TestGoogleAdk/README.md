<!-- omit in toc -->
# Test - Google ADK

<!-- omit in toc -->
## Table of contents

- [Tools](#tools)
- [Steps](#steps)
- [Resources](#resources)
- [Appendix](#appendix)

## Tools

## Steps

- Setup env & install ADK.

  ``` bash
  # Create env.
  python3 -m venv .venv
  # Activate virtual env in Linux.
  source .venv/bin/activate
  # Install ADK.
  pip install google-adk
  # Install required packages.
  pip install -r ./requirements.txt
  ```

- Create project.

  ``` bash
  mkdir multi_tool_agent/
  echo "from . import agent" > multi_tool_agent/__init__.py
  touch multi_tool_agent/agent.py
  touch multi_tool_agent/.env
  ```

- Setup the model.
  - Get an API key from Google AI Studio.
  - Update API key in `.env` file.

- Run agent in 3 ways.

  ``` bash
  # Go back to parent folder of `multi_tool_agent/`.
  cd ..
  # Option 1. Dev UI (adk web)
  adk web
  # Option 2. Terminal (adk run)
  adk run multi_tool_agent
  # Option 3. API server (adk api_server)
  adk api_server
  ```

  - Option 1. Dev UI
    - Open the URL (`http://localhost:8000` or `http://127.0.0.1:8000`).
    - Select project folder.
    - Start to chat with agent.

## Resources

- [Google ADK](https://google.github.io/adk-docs/)
- [Google AI Studio](https://aistudio.google.com/)

## Appendix

- Create virtial env & install packages.

  ```bash
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
  pip freeze > requirements_freeze.txt
  # Upgrade pip.
  python3 -m pip install --upgrade pip
  ```
