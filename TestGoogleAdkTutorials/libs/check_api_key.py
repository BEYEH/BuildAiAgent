import os


def check_api_key():
    if os.environ.get("GOOGLE_API_KEY"):
        print("API Key set.")
    else:
        print("API Key missing.")
