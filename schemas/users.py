from pydantic import BaseModel

class UserCreate(BaseModel):
    Login: str
    Password: str
    Description: str
    
class UserLogin(BaseModel):
    Login:str
    Password:str
    Data:str
    
    