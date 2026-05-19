import sqlite3

DATABASE_NAME = "database/scheduler.db"

def get_connection():

    connection = sqlite3.connect(
        DATABASE_NAME
    )

    return connection


def initialize_database():

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""

        CREATE TABLE IF NOT EXISTS tasks (

            task_id TEXT PRIMARY KEY,

            user_id TEXT,

            priority INTEGER,

            state TEXT,

            retries INTEGER,

            duration REAL
        )

    """)

    connection.commit()

    connection.close()

def save_task(task):

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""

        INSERT INTO tasks (

            task_id,
            user_id,
            priority,
            state,
            retries,
            duration

        )

        VALUES (?, ?, ?, ?, ?, ?)

    """, (

        task.task_id,

        task.user_id,

        task.priority,

        task.state.value,

        task.retry_count,

        task.duration
    ))

    connection.commit()

    connection.close()

def update_task(task):

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""

        UPDATE tasks

        SET

            state = ?,
            retries = ?,
            duration = ?

        WHERE task_id = ?

    """, (

        task.state.value,

        task.retry_count,

        task.duration,

        task.task_id
    ))

    connection.commit()

    connection.close()
def get_all_tasks():

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""

        SELECT
            task_id,
            user_id,
            priority,
            state,
            retries,
            duration

        FROM tasks

    """)

    rows = cursor.fetchall()

    connection.close()

    tasks = []

    for row in rows:

        tasks.append({

            "task_id": row[0],

            "user_id": row[1],

            "priority": row[2],

            "state": row[3],

            "retries": row[4],

            "duration": row[5]
        })

    return tasks