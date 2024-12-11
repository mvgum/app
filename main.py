from fastapi import FastAPI, Path, HTTPException, Request
from app.routers import task
from app.routers import user

app = FastAPI(swagger_ui_parameters={"tryItOutEnabled": True}, debug=True)


@app.get("/")
async def get_mess():
    return {"message": "Welcome to Taskmanager"}

app.include_router(task.router)
app.include_router(user.router)
