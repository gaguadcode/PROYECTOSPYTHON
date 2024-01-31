from langchain_openai import ChatOpenAI
import asyncio
import sys
from dotenv import load_dotenv
import os

# Primero autenticamos el usuario :
# Cargar variables de entorno
load_dotenv()

# Configurar el motor de OpenAI
engine = "gpt-3.5-turbo"
api_key = os.getenv("OPENAI_API_KEY")
model = ChatOpenAI(api_key=api_key)
chunks = []

async def chatear():
    count = 0
    async for chunk in model.astream("hello. tell me something about yourself"):
        chunks.append(chunk)
        count += 1
        print(chunk.content, end="|", flush=True)
    print(f'\n la respuesta consta de {count} tokens')

if __name__ == "__main__":
    asyncio.run(chatear())