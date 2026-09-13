from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"welcome to fats api -- avinash.. good job.."}
