import time
from langchain_ollama import ChatOllama
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

llm = ChatOllama(model='qwen3:1.7b')

def time_function(func):
    def wrapper(*arg, **kwarg):
        start_time = time.time()
        result = func(*arg, **kwarg)
        end_time = time.time()
        total_time = round(end_time - start_time, 2)
        print("Time Taken: ", total_time)
        return result
    return wrapper

history = []
system_message =  SystemMessage("You are a Web Designer. Answer in 1-2 sentences. Give only the direct answer. Never explain step-by-step unless explicitly asked.")

history.append(system_message)

@time_function
def chat(query):
    history.append(HumanMessage(content=query))

    result = llm.invoke(history).content
    history.append(AIMessage(content = result))
    
    print("AI Message: ", result)

while True:
    query = input("Your Message: ")
    if query == "end":
        break
    chat(query)    


print("----Message History----")
print("//n", history)