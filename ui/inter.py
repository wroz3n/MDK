def show_menu():
    print("1. Добавить задачу\n2. Показать все задачи\n3. Изменить статус\n4. Удалить задачу\n5. Поиск задач\n6. Поиск задач (категория/приоритет)\n7. Выход")

def show_task(task):
    print(f"\nID: {task.id}")
    print(f"Название: {task.title}")
    print(f"Описание: {task.description}")
    print(f"Статус: {task.status}")
    print(f"Дата создания: {task.createtime}")
    print(f"Срок выполнения: {task.deadline}")
    print(f"Приоритет: {task.priority}")
    print(f"Категория: {task.category}")