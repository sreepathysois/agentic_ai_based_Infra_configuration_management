import os
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    #model="gpt-4o-mini",
    #temperature=0,
    #api_key=os.getenv("OPENAI_API_KEY")
    model="llama3",
    openai_api_base="http://172.16.18.235:11434/v1",
    openai_api_key="ollama",
    temperature=0
)
