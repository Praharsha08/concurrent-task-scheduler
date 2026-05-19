
from scheduler.states import TaskState
from scheduler.logger import logger



class Task:

    def __init__(
        self,
        priority,
        task_id,
        user_id,
        func,
        dependencies=None,
        retries=0
    ):

        self.priority = priority

        self.task_id = task_id

        self.user_id = user_id

        self.func = func

        self.dependencies = dependencies or []

        self.max_retries = retries

        self.retry_count = 0

        self.state = TaskState.PENDING

        self.start_time = None

        self.end_time = None

        self.duration = None

    def update_state(self, new_state):

        old_state = self.state

        self.state = new_state

        logger.info(
            f"{self.task_id}: "
            f"{old_state.value} -> "
            f"{new_state.value}"
        )

    def __lt__(self, other):

        return self.priority > other.priority