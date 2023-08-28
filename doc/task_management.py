from typing import List
import asyncio
from abc import ABC, abstractmethod

class Task(ABC):
    """An abstract base class representing a task to be executed."""

    def __init__(self, description: str):
        self.description = description
        self.completed = False

    @abstractmethod
    async def execute(self):
        pass


class TaskManager:
    def __init__(self):
        self.tasks: List[Task] = []

    def add_task(self, task: Task):
        self.tasks.append(task)

    async def run_tasks(self):
        await asyncio.gather(*[task.execute() for task in self.tasks])


class SimpleTask(Task):
    async def execute(self):
        await asyncio.sleep(1)
        self.completed = True
        # this simple example just print something, nothing else
        # TODO create something that is really useful
        print(f"Completed task: {self.description}")


if __name__ == "__main__":
    task_manager = TaskManager()

    task1 = SimpleTask("Write report")
    task2 = SimpleTask("Send emails")

    task_manager.add_task(task1)
    task_manager.add_task(task2)

    asyncio.run(task_manager.run_tasks())
