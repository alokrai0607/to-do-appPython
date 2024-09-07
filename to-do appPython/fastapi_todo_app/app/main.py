from fastapi import FastAPI
from app.controllers import todo_controller
from app.config import init_db
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse

app = FastAPI()

@app.get("/favicon.ico")
async def favicon():
    return FileResponse("path_to_favicon/favicon.ico")

@app.on_event("startup")
def startup_event():
    init_db()
 
app.include_router(todo_controller.router)

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["*"],  # Allow all origins for development; adjust for production
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/todos")
def get_todos():
    pass

@app.post("/todos")
def create_todo():
    pass

@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    pass
