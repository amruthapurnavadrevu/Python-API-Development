from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return "Hello! This is FastAPI! I'm learning things"