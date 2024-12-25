from fastapi import FastAPI
from controller import bot
import os
import asyncio
import uvicorn
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()
TOKEN = os.environ.get("TOKEN")

@app.get("/")
async def root():
    return {"hello":"HELLO"}

@app.on_event("startup")
async def startup():
    asyncio.create_task(bot.start(TOKEN))

@app.on_event("shutdown")
async def shutdown():
    await bot.stop()

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)