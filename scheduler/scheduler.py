import heapq
import threading
import time

from concurrent.futures import ThreadPoolExecutor

from scheduler.states import TaskState
from scheduler.dependency_manager import DependencyManager
from scheduler.logger import logger
from database.db import update_task


class TaskScheduler:

    def __init__(self, max_workers=3):

        self.max_workers = max_workers

        # Priority queue
        self.task_queue = []

        # Store all tasks
        self.tasks = {}

        # Track completed tasks
        self.completed_tasks = set()

        # Track failed tasks
        self.failed_tasks = set()

        self.running_tasks = set()

        self.active_workers = 0

        # Thread safety lock
        self.lock = threading.Lock()

        # Worker pool
        self.executor = ThreadPoolExecutor(
            max_workers=max_workers
        )

        # Dependency handler
        self.dependency_manager = DependencyManager()

    def add_task(self, task):

        self.tasks[task.task_id] = task

        # No dependencies -> ready immediately
        if not task.dependencies:

            task.update_state(TaskState.READY)

            with self.lock:

                heapq.heappush(
                    self.task_queue,
                    task
                )

        else:

            logger.info(
                f"Task {task.task_id} "
                f"waiting for dependencies"
            )

    def resolve_dependencies(self):

        for task in self.tasks.values():

            # Only check pending tasks
            if task.state != TaskState.PENDING:
                continue

            dependencies_done = (
                self.dependency_manager
                .dependencies_completed(
                    task,
                    self.completed_tasks
                )
            )

            if dependencies_done:

                logger.info(
                    f"Dependencies resolved "
                    f"for {task.task_id}"
                )

                task.update_state(
                    TaskState.READY
                )

                with self.lock:

                    heapq.heappush(
                        self.task_queue,
                        task
                    )

    def execute_task(self, task):

        task.update_state(TaskState.RUNNING)

        self.running_tasks.add(task.task_id)

        self.active_workers += 1

        task.start_time = time.time()

        try:

            logger.info(
                f"Executing task "
                f"{task.task_id}"
            )

            # Execute actual function
            task.func()

            task.end_time = time.time()

            task.duration = (task.end_time - task.start_time)

            task.update_state(
                TaskState.COMPLETED
            )
            self.running_tasks.remove(task.task_id)

            self.active_workers -= 1

            update_task(task)

            logger.info(
                f"Task {task.task_id} "
                f"completed successfully"
            )

            with self.lock:

                self.completed_tasks.add(
                    task.task_id
                )

        except Exception as e:
            
            task.end_time = time.time()

            task.duration = (
            task.end_time - task.start_time
            )
            logger.error(
                f"Task {task.task_id} "
                f"failed: {e}"
            )

            task.retry_count += 1

            # Retry available
            if (
                task.retry_count
                <= task.max_retries
            ):

                logger.warning(
                    f"Retrying "
                    f"{task.task_id} "
                    f"({task.retry_count}/"
                    f"{task.max_retries})"
                )

                task.update_state(
                    TaskState.READY
                )
                update_task(task)

                with self.lock:

                    heapq.heappush(
                        self.task_queue,
                        task
                    )

            else:

                task.update_state(
                    TaskState.FAILED
                )

                if task.task_id in self.running_tasks:

                    self.running_tasks.remove(task.task_id)

                self.active_workers -= 1

                update_task(task)

                logger.error(
                    f"Task {task.task_id} "
                    f"permanently failed"
                )

                with self.lock:

                    self.failed_tasks.add(
                        task.task_id
                    )

    "{task.duration:.2f} seconds"
    def run(self):

    # Validate DAG
        has_cycle = (
            self.dependency_manager
            .detect_cycle(self.tasks)
        )

        if has_cycle:

            raise Exception(
                "Cycle detected in task dependencies"
            )

        logger.info(
            "Scheduler started"
        )

        while True:

            # Move dependency-resolved tasks
            self.resolve_dependencies()

            with self.lock:

                # No ready tasks
                if not self.task_queue:

                    unfinished_tasks = [

                        task

                        for task
                        in self.tasks.values()

                        if task.state not in (
                            TaskState.COMPLETED,
                            TaskState.FAILED
                        )
                    ]

                    # Keep scheduler alive
                    if not unfinished_tasks:

                        time.sleep(1)

                        continue

                    continue

                # Get highest-priority task
                task = heapq.heappop(
                    self.task_queue
                )

            # Execute concurrently
            self.executor.submit(
                self.execute_task,
                task
            )

        self.executor.shutdown(wait=True)

        logger.info(
            "Scheduler finished"
        )

        print("\n===== EXECUTION SUMMARY =====")

        print(
            f"Completed Tasks: "
            f"{self.completed_tasks}"
        )

        print(
            f"Failed Tasks: "
            f"{self.failed_tasks}"
        )

        print("\n===== TASK METRICS =====")

        for task in self.tasks.values():

            print(f"\nTask: {task.task_id}")

            print(f"State: {task.state.value}")

            print(f"Retries: {task.retry_count}")

            if task.duration:

                print(
                    f"Duration: "
                    f"{task.duration:.2f} seconds"
                )          