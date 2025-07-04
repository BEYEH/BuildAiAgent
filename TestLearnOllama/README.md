<!-- omit in toc -->
# Test - Learn Ollama

<!-- omit in toc -->
## Table of contents

- [Note](#note)
- [Pathway](#pathway)
- [Resources](#resources)

## Note

- Hardware requirement

  | RAM (GB) | Parameters of Models (B) |
  | :------: | :----------------------: |
  |    8     |            7             |
  |    16    |            13            |
  |    32    |            33            |

## Pathway

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

- Ollama

  ```bash
  # Download.
  curl -fsSL https://ollama.com/install.sh |
  # Check.
  ollama
  # Check models.
  ollama list
  # Install Ollama models.
  ollama pull llama3.2
  ollama pull mxbai-embed-large
  ```

## Resources

- GitHub
  - [ollama / ollama](https://github.com/ollama/ollama)
- YouTube
  - [Learn Ollama in 15 Minutes - Run LLM Models Locally for FREE](https://www.youtube.com/watch?v=UtSSMs6ObqY)
