from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from langchain_ollama import ChatOllama
from dotenv import load_dotenv

load_dotenv()

llm = ChatOllama(model='')

message= [ 
    SystemMessage("You are a Professional Fashion Designer"),
    HumanMessage("What types of Design are there in market")
]

result = llm.invoke(message)

print(result.content)