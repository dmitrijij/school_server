from pydantic import BaseModel

class Message(BaseModel):
    ID: int
    Text:str
    Date:str