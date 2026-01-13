from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(
    vertexai= True,
    project="aws-prod-484205"
)

def main():
    response = client.models.generate_content(
        model="gemini-2.0-flash-exp",
        contents="Explain how AI works in a few words"
    )
    print(response.text)


if __name__ == "__main__":
    main()
