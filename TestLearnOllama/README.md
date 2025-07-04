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

- Parameters of model between 10 to 33.

  | Model            | Parameters | Size  | Download                   |
  | ---------------- | :--------: | :---: | -------------------------- |
  | QwQ              |    32B     | 20GB  | ollama run qwq             |
  | Gemma 3          |    27B     | 17GB  | ollama run gemma3:27b      |
  | Phi 4            |    14B     | 9.1GB | ollama run phi4            |
  | Gemma 3          |    12B     | 8.1GB | ollama run gemma3:12b      |
  | Llama 3.2 Vision |    11B     | 7.9GB | ollama run llama3.2-vision |

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
