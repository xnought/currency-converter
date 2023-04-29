from fastapi import FastAPI
from uvicorn import run
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
def index():
    return {"message": "Hello, world!"}


if __name__ == "__main__":
    run(app, host="localhost", port=8000)
