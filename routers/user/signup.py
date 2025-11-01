from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.users import UserCreate
from model.users_model import User
from base.user_db import get_db

router = APIRouter(prefix="/user", tags=["sign up"])

@router.post("/sign-up/")
async def signup(user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.Login == user.Login).first()
    if db_user:
        raise HTTPException(status_code=400, detail="The user already exists")
    

    new_user = User(
        Login=user.Login,
        Password=user.Password,
        Description=user.Description,
    )
    
    db.add(new_user)    
    db.commit()
    db.refresh(new_user)
    
    return {"message": "User created successfully", "login": new_user.Login}