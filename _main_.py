from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)

from langchain.chat_models import ChatOpenAI


load_dotenv()

app=FastAPI()

class Item(BaseModel):
    question:str
    
@app.post('/talkwithme')
async def asknormalquestion(item : Item):
    chat = ChatOpenAI(model_name="gpt-3.5-turbo",temperature=0.3)
    messages = [
    SystemMessage(content="You are a bot with good knowledge"),
    HumanMessage(content=item.question)
]
    response = chat(messages)
    return response.content

