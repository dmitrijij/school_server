from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session
from model.users_model import User


from base.user_db import get_db

router=APIRouter(prefix="/user", tags=["fbus"])

@router.get("/fbus/")
async def get_by_id(login,db: Session = Depends(get_db)):
    res=(db.query(User).filter(User.Login == login).first())
    if res!=0:
        return res
    else: raise HTTPException(detail="The user not exists")
    