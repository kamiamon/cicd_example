from fastapi import FastAPI, Query
import uvicorn
import os

app = FastAPI()

@app.get("/")
def root():
    return {"msg": "Hello World!"}

@app.get("/read-file")
def read_file(path: str = Query(..., description="Path to the file to read")):
    try:
        with open(path, "r") as file:
            content = file.read()
        return {"content": content}
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
