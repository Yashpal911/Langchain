from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from langchain_ollama import ChatOllama
from dotenv import load_dotenv
import time

load_dotenv()



def time_period(func):
    def wrapper(*arg, **kwargs):
        start_time = time.time()
        result = func(*arg, **kwargs)
        end_time = time.time()
        total_time = end_time - start_time
        print("Total time taken to complete: ", round(total_time, 2))
        return result
    return wrapper



llm = ChatOllama(model="qwen3:1.7b")

message= [ 
    SystemMessage("You are a concise AI assistant. Answer in 1-2 sentences. Give only the direct answer. Never explain step-by-step unless explicitly asked."),
    HumanMessage("What is the squareroot of 49")
]

@time_period
def chat():
    result = llm.invoke(message)
    print(result.content)
    return 1

chat();