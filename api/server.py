import threading

from scheduler.scheduler import TaskScheduler
from scheduler.task import Task

from fastapi import (
    FastAPI,
    Request
)

from fastapi.templating import Jinja2Templates

from database.db import (
    initialize_database,
    save_task
)

from api.task_functions import (
    download_task,
    clean_task,
    report_task
)
app = FastAPI()

templates = Jinja2Templates(
    directory="templates"
)
scheduler = TaskScheduler(max_workers=3)

initialize_database()

TASK_FUNCTIONS = {

    "download": download_task,

    "clean": clean_task,

    "report": report_task
}

def serialize_task(task):

    return {

        "task_id": task.task_id,

        "user_id": task.user_id,

        "priority": task.priority,

        "state": task.state.value,

        "retries": task.retry_count,

        "dependencies": task.dependencies,

        "duration": task.duration
    }

@app.get("/")
def home():

    return {
        "message": "Concurrent Task Scheduler API"
    }

@app.post("/tasks")
def create_task(task_data: dict):

    task_type = task_data["task_type"]

    if task_type not in TASK_FUNCTIONS:

        return {
            "error": "Invalid task type"
        }

    task = Task(

        priority=task_data["priority"],

        task_id=task_data["task_id"],

        user_id=task_data["user_id"],

        func=TASK_FUNCTIONS[task_type],

        dependencies=task_data.get(
            "dependencies",
            []
        ),

        retries=task_data.get(
            "retries",
            0
        )
    )

    scheduler.add_task(task)
    save_task(task)

    return {
        "message": f"Task "
                   f"{task.task_id} added"
    }

@app.get("/tasks")
def get_tasks():

    return [

        serialize_task(task)

        for task in scheduler.tasks.values()
    ]

@app.get("/tasks/{task_id}")
def get_task(task_id: str):

    task = scheduler.tasks.get(task_id)

    if not task:

        return {
            "error": "Task not found"
        }

    return serialize_task(task)

def run_scheduler():

    scheduler.run()

@app.get("/status")
def get_status():

    return {

        "total_tasks": len(
            scheduler.tasks
        ),

        "completed_tasks": len(
            scheduler.completed_tasks
        ),

        "failed_tasks": len(
            scheduler.failed_tasks
        ),

        "queued_tasks": len(
            scheduler.task_queue
        )
    }

scheduler_thread = threading.Thread(
    target=run_scheduler,
    daemon=True
)

scheduler_thread.start()

@app.get("/dashboard")
def dashboard(request: Request):

    tasks = [
        serialize_task(task)
        for task in scheduler.tasks.values()
    ]

    return templates.TemplateResponse(

        request=request,

        name="dashboard.html",

        context={

            "tasks": tasks,

            "total_tasks": len(
                scheduler.tasks
            ),

            "completed_tasks": len(
                scheduler.completed_tasks
            ),

            "failed_tasks": len(
                scheduler.failed_tasks
            ),

            "queued_tasks": len(
                scheduler.task_queue
            )
        }
    )