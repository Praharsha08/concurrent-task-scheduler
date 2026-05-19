from enum import Enum


class TaskState(Enum):

    PENDING = "PENDING"

    READY = "READY"

    RUNNING = "RUNNING"

    COMPLETED = "COMPLETED"

    FAILED = "FAILED"

    CANCELLED = "CANCELLED"