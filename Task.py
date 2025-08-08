"""
Создай класс `Task`, который позволяет управлять задачами (делами).
У задачи должны быть атрибуты: описание задачи, срок выполнения и статус (выполнено/не выполнено). Реализуй функцию для добавления задач,
отметки выполненных задач и вывода списка текущих (не выполненных) задач.
"""

from datetime import date

"""Represents a task with description, due date, and status."""
class Task():

    def __init__(self, description: str, due_date: date):
        self.description = description
        self.due_date = due_date
        self.completed = False

    def mark_completed(self):
        """Mark the task as completed."""
        self.completed = True

    def __str__(self):
        status = "Completed" if self.completed else "Pending"
        return f"{self.description} (Due: {self.due_date}, Status: {status})"


"""Manages a list of tasks."""
class TaskManager:


    def __init__(self):
        self.tasks = []

    def add_task(self, description: str, due_date: date):
        """Add a new task."""
        task = Task(description, due_date)
        self.tasks.append(task)

    def mark_task_completed(self, index: int):
        """Mark the task at the given index as completed."""
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_completed()

    def get_pending_tasks(self):
        """Return a list of all pending (not completed) tasks."""
        return [task for task in self.tasks if not task.completed]

    def show_pending_tasks(self):
        """Print all pending tasks."""
        pending = self.get_pending_tasks()
        if not pending:
            print("No pending tasks.")
        else:
            for i, task in enumerate(pending, start=1):
                print(f"{i}. {task}")


# Example usage
if __name__ == "__main__":
    manager = TaskManager()
    manager.add_task("Submit VAT return", date(2025, 8, 10))
    manager.add_task("Prepare payroll report", date(2025, 8, 15))

    print("Pending tasks:")
    manager.show_pending_tasks()

    # Mark the first task as completed
    manager.mark_task_completed(0)

    print("\nPending tasks after completion:")
    manager.show_pending_tasks()