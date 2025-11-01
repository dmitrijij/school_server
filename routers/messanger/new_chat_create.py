from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session

import sqlite3

from base.chat_db import get_db
from base.concret_chats_db import init_db

from schemas.message import newChat

router=APIRouter(prefix="/chat/",tags=["chat"])

@router.post("/newChat")
def NewChat(newchat:newChat,db:Session=Depends(get_db)):
    existing_chat = db.query(newChat).filter(
        (newChat.FirstPerson == newchat.FirstPerson & newChat.SecondPerson == newchat.SecondPerson) |
        (newChat.FirstPerson == newchat.SecondPerson & newChat.SecondPerson == newchat.FirstPerson)
    ).first()
    
    if existing_chat:
        raise HTTPException(
            status_code=400
        )
    NewpChat=newChat(newchat.FirstPerson,newchat.SecondPerson)
    
    db.add(NewpChat)
    db.commit()
    db.refresh(NewpChat)  
    
    element_id = db.query(newChat.id).filter(
    newChat.FirstPerson == NewpChat.FirstPerson,
    newChat.SecondPerson == NewpChat.SecondPerson
    ).scalar()
    
    
    init_db(element_id)
    
    
    
    raise HTTPException(status_code=200) 