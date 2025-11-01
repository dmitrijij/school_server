from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session
from model.users_model import User


from base.user_db import get_db

router=APIRouter(prefix="/user", tags=["gbid"])

@router.get("/gbid/")
async def get_by_id(id,db: Session = Depends(get_db)):
    res=(db.query(User).filter(User.ID == id).first())
    if res!=0:
        return(db.query(User).filter(User.ID == id).first())
    else: raise HTTPException(detail="The user not exists")
    