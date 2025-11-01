from fastapi import FastAPI
import uvicorn

from base.user_db import init_db as init_user_db
from base.chat_db import init_db as init_chat_db

from routers import ping
from routers.user import signin, signup, fbus, fbid,getallusers

init_user_db()
init_chat_db()

app = FastAPI()

app.include_router(ping.router)
app.include_router(signup.router)
app.include_router(signin.router)
app.include_router(fbus.router)
app.include_router(fbid.router)
app.include_router(getallusers.router)

@app.get("/")
async def root():
    return {"message": "Server is running"}

if __name__ == "__main__":
    uvicorn.run(
        app, 
        host="0.0.0.0", 
        port=8000   
    )