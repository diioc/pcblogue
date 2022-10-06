from fastapi import FastAPI

app = FastAPI()

@app.get("/get_some/{some_value}")
async def get_started(some_value: str):
    return {"got_some": some_value}