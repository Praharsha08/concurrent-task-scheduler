import random
import time

from scheduler.task import Task
from scheduler.scheduler import TaskScheduler


def download_data():

    print("Downloading Data...")

    time.sleep(2)

    print("Download Complete")


def clean_data():

    print("Cleaning Data...")

    time.sleep(2)

    if random.choice([True, False]):

        raise Exception("Data cleaning error")

    print("Cleaning Complete")


def train_model():

    print("Training Model...")

    time.sleep(3)

    print("Training Complete")


def generate_report():

    print("Generating Report...")

    time.sleep(1)

    print("Report Generated")


scheduler = TaskScheduler(max_workers=3)


scheduler.add_task(
    Task(
        priority=1,
        task_id="download",
        user_id="user_1",
        func=download_data,
        retries=1
    )
)

scheduler.add_task(
    Task(
        priority=2,
        task_id="clean",
        user_id="user_1",
        func=clean_data,
        dependencies=["download"],
        retries=2
    )
)

scheduler.add_task(
    Task(
        priority=3,
        task_id="train",
        user_id="user_1",
        func=train_model,
        dependencies=["clean"],
        retries=1
    )
)

scheduler.add_task(
    Task(
        priority=4,
        task_id="report",
        user_id="user_1",
        func=generate_report,
        dependencies=["train"],
        retries=1
    )
)

scheduler.run()