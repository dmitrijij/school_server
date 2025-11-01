from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session
from model.chat_model import Chat
from schemas.message import Message

from base.chat_db import get_db

router=APIRouter(prefix="/chat",tags=["messanger"])

# @router.post("/send_message/")
# def send_message(message:Message,db: Session=Depends(get_db)):
#     new_message=Message(message.ID,message.Text,message.Date)
#     db.add(new_message)
    