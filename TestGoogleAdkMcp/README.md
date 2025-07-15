<!-- omit in toc -->
# Test - Google ADK MCP

<!-- omit in toc -->
## Table of contents

- [Target](#target)
- [App Screenshots](#app-screenshots)
- [Steps](#steps)
- [Note](#note)
- [Resources](#resources)

## Target

## App Screenshots

## Steps

- Setup env & install ADK.

  ```bash
  mkdir TestGoogleAdkMcp
  cd TestGoogleAdkMcp
  touch requirements.txt
  python -m venv .venv
  source .venv/bin/activate
  pip list
  pip install -r ./requirements.txt
  pip freeze > requirements_freeze.txt
  ```

## Note

## Resources

- Google ADK
  - [Get Started](https://google.github.io/adk-docs/get-started/)
  - [Model Context Protocol (MCP)](https://google.github.io/adk-docs/mcp/)
  - [Model Context Protocol Tools](https://google.github.io/adk-docs/tools/mcp-tools/)
- Google AI for Developers
  - [All models](https://ai.google.dev/gemini-api/docs/models)
- Google AI Studio
  - [API Keys](https://aistudio.google.com/app/apikey)
