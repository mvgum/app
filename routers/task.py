from fastapi import FastAPI, Path, HTTPException, Request, APIRouter

router = APIRouter(prefix='/task', tags=['task'])


@router.get("/")
async def all_tasks():
    pass
    # return templates.TemplateResponse('users.html', {'request': request, 'users': users})


@router.get("/task_id")
async def task_by_id():
    pass


@router.post("/create")
async def create_task():
    pass


@router.put("/update")
async def update_task():
    pass


@router.delete("/delete")
async def delete_task():
    pass
