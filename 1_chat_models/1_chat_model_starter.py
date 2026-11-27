from langchain_ollama import ChatOllama
from dotenv import load_dotenv
import time
# For Open AI
# from langchain_openai import ChatOpenAI

load_dotenv()

# For Open AI
# llm = ChatOpenAI(model="GPT-6 Luna")


llm = ChatOllama(
    # model="qwen3:4b",
    model="qwen3:1.7b",
    temperature=0.7,
    think=False
)

start_time = time.time()
print("we are using model:", llm.model)
print("this is started")

result = llm.invoke("What is the square root of 49")
end_time = time.time()


total_time = end_time - start_time

print("Result: ",result.content, f"//n")
print("Time Taken :", round(total_time, 2))
