import logging


logging.basicConfig(
    filename="logs/scheduler.log",
    level=logging.INFO,
    format=(
        "%(asctime)s "
        "[%(levelname)s] "
        "%(message)s"
    )
)

logger = logging.getLogger("scheduler")