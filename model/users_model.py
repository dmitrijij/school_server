from sqlalchemy import Column, Integer, String
from base.user_db import Base

class User(Base):
    __tablename__ = "user"
    
    ID = Column(Integer, primary_key=True, autoincrement=True, index=True)
    Login = Column(String, unique=True, nullable=False)
    Password = Column(String, nullable=False)
    Description = Column(String,nullable=True)
    ChatConsist = Column(String,nullable=True)