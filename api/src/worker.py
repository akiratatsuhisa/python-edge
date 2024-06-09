from fastapi import FastAPI, Request
from pydantic import BaseModel


async def on_fetch(request, env):
    import asgi

    return await asgi.fetch(app, request, env)


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "ping!"}


@app.get("/ai")
async def root(req: Request):
    return {"ai": "test"}
