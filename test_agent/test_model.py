from config.model import llm

response = llm.invoke("Hello, introduce yourself in one sentence.")

print(response.content)