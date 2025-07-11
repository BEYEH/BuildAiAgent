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

## Resources

- [Google ADK](https://google.github.io/adk-docs/)

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
