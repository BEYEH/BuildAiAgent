from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()


def main():
    llm = ChatGroq(model="llama-3.3-70b-versatile")

    query = input("User Input: ")

    messages = [
        (
            "system",
            """
            You are a helpful assistant that translates English to Traditional Chinese. 
            Translate the user sentence.
            """,
        ),
        ("human", query),
    ]

    ai_msg = llm.invoke(messages)
    print(ai_msg)


if __name__ == "__main__":
    main()
