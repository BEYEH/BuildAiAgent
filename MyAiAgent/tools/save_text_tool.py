import os
from langchain.tools import tool
from datetime import datetime

@tool
def t_save_text_to_file(data: str) -> str:
    """Save text data to a local file with timestamp."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted_text = f"--- Research Output ---\nTimestamp: {timestamp}\n\n{data}\n\n"

    filename = os.path.join(os.getcwd(), "research_output.txt")
    with open(filename, "a", encoding="utf-8") as f:
        f.write(formatted_text)

    return f"Data successfully saved to {filename}"
