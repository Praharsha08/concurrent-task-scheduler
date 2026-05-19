class DependencyManager:

    def dependencies_completed(
        self,
        task,
        completed_tasks
    ):

        for dependency in task.dependencies:

            if dependency not in completed_tasks:

                return False

        return True

    def detect_cycle(self, tasks):

        visited = set()

        recursion_stack = set()

        def dfs(task_id):

            # Already in current path
            if task_id in recursion_stack:
                return True

            # Already fully checked
            if task_id in visited:
                return False

            visited.add(task_id)

            recursion_stack.add(task_id)

            task = tasks[task_id]

            for dependency in task.dependencies:

                if dependency not in tasks:

                    raise Exception(
                        f"Dependency '{dependency}' "
                        f"does not exist"
                    )

                if dfs(dependency):
                    return True

            recursion_stack.remove(task_id)

            return False

        # Check every task
        for task_id in tasks:

            if dfs(task_id):
                return True

        return False