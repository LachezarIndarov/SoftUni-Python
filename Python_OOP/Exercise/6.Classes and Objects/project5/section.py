# This is file for 5.To-do List
class Section:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, task):
        if task in self.tasks:
            return f"Task is already in the section {self.name}"
        self.tasks.append(task)
        return f"Task {task.details()} is added to the section"

    def complete_task(self, task_name):
        for task in self.tasks:
            if task.name == task_name:
                task.completed = True
                return f"Completed task {task_name}"
        return f"Could not find task with the name {task_name}"

    """ Variant1
    def clean_section(self):

        removed_counter = 0
        for task in self.tasks:
            if task.completed:
                self.task.remove(task)
                removed_counter += 1
        return f"Cleared {removed_counter} tasks."
    """
    # Variant2
    def clean_section(self):
        initial_len = len(self.tasks)
        self.tasks = [t for t in self.tasks if not t.completed]
        return f"Cleared {initial_len - len(self.tasks)} tasks."

    def view_section(self):
        result = f'Section {self.name}:\n'
        for task in self.tasks:
            result += task.details() + '\n'
            return result.strip()

