from database.DB import load_tasks_dict,load_tasks_list, save_task, delete_task
from src.task import Task
from datetime import datetime
class TaskManager:
    def __init__(self): 
        self.tasks_list = load_tasks_list()  
    def create_task(self, title, description, deadline, priority, category):
        new_task = Task(
            task_id=None,
            title=title,
            description=description,
            createtime=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            status='не выполнено',
            deadline=deadline,
            priority=priority,
            category=category
        )
        saved_task = save_task(new_task)
        self.tasks_dict[saved_task.id] = saved_task  # Сохраняем в словаре
        self.tasks_list.append(saved_task)  # Добавляем в список
        return saved_task

    def delete_task(self, task_id):
        if task_id in self.tasks_dict:
            delete_task(task_id)  # удаляем задачу
            del self.tasks_dict[task_id]  # Удаляем задачу из словаря
            self.tasks_list = [task for task in self.tasks_list if task.id != task_id]  # Удаляем из списка
            return True
        return False
    def get_all_tasks(self):
        return self.tasks_list
    def update_task(self, task_id, title=None, description=None, status=None, deadline=None, priority=None, category=None):
        if task_id in self.tasks_dict:
            task_data = self.tasks_dict[task_id]
            task = Task(
                task_id=task_data.id,
                title=title if title else task_data.title,
                description=description if description else task_data.description,
                createtime=task_data.createtime,
                status=status if status else task_data.status,
                deadline=deadline if deadline else task_data.deadline,
                priority=priority if priority else task_data.priority,
                category=category if category else task_data.category
            )
            save_task(task)
            self.tasks_dict[task_id] = task
            self.tasks_list = [t for t in self.tasks_list if t.id != task_id]  # Удаляем старую задачу из списка
            self.tasks_list.append(task) 
            return True
        return False

    def get_task(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None
    def search_task(self, search_term):
        results = []
        for task in self.get_all_tasks():
            if (search_term.lower() in task.title.lower() or
                    search_term.lower() in task.description.lower() or
                    search_term.lower() in task.status.lower() or
                    search_term.lower() in task.priority.lower() or
                    search_term.lower() in task.category.lower()):
                results.append(task)
        return results
    def search_task_cp(self, search_term):
        results = []
        for task in self.get_all_tasks():
            if (search_term.lower() in task.priority.lower() or
                    search_term.lower() in task.category.lower()):
                results.append(task)
        return results
