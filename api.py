from fastapi import FastAPI
from pydantic import BaseModel
from operator import itemgetter
from automation.app import clickBtn
from pymongo import MongoClient
from dotenv import load_dotenv

connectionStr = load_dotenv("CONNECTION_STRING_MONGODB")

class LoginCredentials(BaseModel):
    email:str
    password:str
    loginTime:str
    logoutTime:str


app = FastAPI()
@app.get("/")
async def root():
    return {"msg":"Y u here?"}

@app.post("/login")
async def loginService(loginCredentials:LoginCredentials):
    email, password, loginTime, logoutTime = itemgetter("email", "password", "loginTime", "logoutTime")(loginCredentials)
    print("Logging in...")
    result= clickBtn(email=email, password=password)
    return ({"transaction": {email: email, loginTime: loginTime, logoutTime: logoutTime, result: True if result else False}})
