from sqlalchemy import Column, Integer, String, DateTime, Boolean
from base.chat_db import Base

class overchat(Base):
    IDchat=Column("chatID",Integer,primary_key=True,index=True)
    FirstPerson=Column("firstP",Integer)
    SecondPerson=Column("secondP"<Integer)
    # Isblocked=Column("block",Integer,nullable=True)
    