<!-- omit in toc -->
# Test - ADK Custom

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
  # Install required packages.
  pip install -r ./requirements.txt
  # Set SSL_CERT_FILE variable.
  export SSL_CERT_FILE=$(python -m certifi)
  # Download sample code.
  git clone --no-checkout https://github.com/google/adk-docs.git
  cd adk-docs
  git sparse-checkout init --cone
  git sparse-checkout set examples/python/snippets/streaming/adk-streaming
  git checkout main
  cd examples/python/snippets/streaming/adk-streaming/app
  ```

## Resources

- [Custom Audio Streaming app (SSE)](https://google.github.io/adk-docs/streaming/custom-streaming/)

## Appendix
