from sqlalchemy import Column, Integer, String, DateTime, Boolean
from base.chat_db import Base

class Chat(Base):
    __tablename__ = "chat"
    number = Column('number', Integer, index=True, primary_key=True) 
    Id = Column('Id', Integer)
    Text = Column('Text', String)
    Date = Column('Data', String)
    isreaded = Column('isreaded', Boolean)
    