from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from model.users_model import User
from base.user_db import get_db
from schemas.users import UserLogin

router = APIRouter(prefix="/user", tags=["sign in"])

@router.post("/sign-in/")
async def signin(user: UserLogin, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(
        User.Login == user.Login,
        User.Password == user.Password
    ).first()
    
    if db_user:
        raise HTTPException(status_code=200)
    else:
        raise HTTPException(status_code=401,detail="неверный логин или пароль")