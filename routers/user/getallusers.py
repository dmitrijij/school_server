from fastapi import APIRouter, HTTPException,Depends
from base.user_db import get_db
from model.users_model import User
from sqlalchemy.orm import Session

router= APIRouter(prefix="/user",tags=["getalluser"])

@router.get("/getallusers")
async def getall(db:Session=Depends(get_db)):
    return(db.query(User).all())
     