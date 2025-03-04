from src.task_manager import TaskManager
from ui.inter import show_menu, show_task
task_manager = TaskManager()
def main():
    print("Добро пожаловать!")
    while True:
        show_menu()
        choice = input("Выберите действие: ")
        if choice == '1':
            add_task()
        elif choice == '2':
            show_all_tasks()
        elif choice == '3':
            update_task_cli()
        elif choice == '4':
            delete_task_cli()
        elif choice == '5':
            search_tasks_cli()
        elif choice == '6':
            search_task_cp_cli()
        elif choice == '7':
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор, попробуйте снова.")

def add_task():
    title = input("Введите название задачи: ")
    description = input("Введите описание задачи: ")
    deadline = input("Введите срок выполнения (Y-M-D H:M:S): ")
    priority = input("Введите приоритет (низкий, средний, высокий): ")
    category = input("Введите категорию (работа, учеба, личное): ")
    task_manager.create_task(title, description, deadline, priority, category)
    print("Задача успешно добавлена!")

def show_all_tasks():
    tasks = task_manager.get_all_tasks()
    for task in tasks:
        show_task(task)

def update_task_cli():
    task_id = int(input("Введите ID задачи для обновления: "))
    title = input("Новое название (оставьте пустым, чтобы не менять): ")
    description = input("Новое описание (оставьте пустым, чтобы не менять): ")
    status = input("Новый статус (оставьте пустым, чтобы не менять): ")
    deadline = input("Новый срок выполнения (оставьте пустым, чтобы не менять): ")
    priority = input("Новый приоритет (оставьте пустым, чтобы не менять): ")
    category = input("Новая категория (оставьте пустым, чтобы не менять): ")
    if task_manager.update_task(
            task_id,
            title if title else None,
            description if description else None,
            status if status else None,
            deadline if deadline else None,
            priority if priority else None,
            category if category else None
    ):
        print("Задача обновлена!")
    else:
        print("Ошибка: задача не найдена")

def delete_task_cli():
    task_id = int(input("Введите ID задачи для удаления: "))
    if task_manager.delete_task(task_id):
        print("Задача удалена!")
    else:
        print("Ошибка: задача не найдена")

def search_tasks_cli():
    search_term = input("Введите поисковый запрос: ")
    results = task_manager.search_task(search_term)
    if results:
        print("Найденные задачи:")
        for task in results:
            show_task(task)
    else:
        print("Задачи не найдены.")

def search_task_cp_cli():
    search_term = input("Введите категорию или приоритет для поиска: ")
    results = task_manager.search_task_cp(search_term)
    if results:
        print("Найденные задачи по категории или приоритету:")
        for task in results:
            show_task(task)
    else:
        print("Задачи не найдены.")