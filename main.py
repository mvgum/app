from fastapi import FastAPI, Path, HTTPException, Request
from routers import task
from routers import user

app = FastAPI(swagger_ui_parameters={"tryItOutEnabled": True}, debug=True)


@app.get("/")
async def get_users():
    return {"message": "Welcome to Taskmanager"}

app.include_router(task.router)
app.include_router(user.router)
