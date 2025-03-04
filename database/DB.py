import sqlite3
from datetime import datetime
# db = sqlite3.connect('database/tasks.db')
from src.task import  Task
def connection():
    cont = None
    try:
        cont = sqlite3.contect('database/tasks.db')
        c = cont.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS taskdb
                     (id INTEGER PRIMARY KEY AUTOINCREMENT,
                      title TEXT,
                      description TEXT,
                      status TEXT DEFAULT 'не выполнено',
                      createtime DATETIME DEFAULT CURRENT_TIMESTAMP,
                      deadline DATETIME,
                      priority TEXT,
                      category TEXT)''')
        cont.commit()
    except Exception as e:
        print(f"Ошибка при подключении к базе данных: {e}")
    return cont

def load_tasks_as_dict():
    cont = connection()
    tasks = {}
    try:
        c = cont.cursor()
        c.execute("SELECT * FROM taskdb")
        rows = c.fetchall()
        for row in rows:
            task = Task(
                task_id=row[0],
                title=row[1],
                description=row[2],
                createtime=row[4],
                status=row[3],
                deadline=row[5],
                priority=row[6],
                category=row[7]
            )

            tasks[task.id] = task

    except Exception as e:

        print(f"Ошибка при загрузке задач: {e}")

    finally:

        if cont:

            cont.close()

    return tasks


def load_tasks_as_list():

    cont = connection()

    tasks = []

    try:
        c = cont.cursor()
        c.execute("SELECT * FROM taskdb")
        rows = c.fetchall()
        for row in rows:
            task = Task(
                task_id=row[0],
                title=row[1],
                description=row[2],
                createtime=row[4],
                status=row[3],
                deadline=row[5],
                priority=row[6],
                category=row[7]
            )

            tasks.append(task)

    except Exception as e:
        print(f"Ошибка при загрузке задач: {e}")
    finally:
        if cont:
            cont.close()
    return tasks
def save_task(task):
    cont = connection()
    try:
        c = cont.cursor()
        if task.id is None:
            c.execute('''INSERT INTO taskdb (title, description, status, createtime, deadline, priority, category)
                         VALUES (?, ?, ?, ?, ?, ?, ?)''',
                      (task.title, task.description,
                       task.status, task.createtime,
                       task.deadline, task.priority, task.category))
            task.id = c.lastrowid
        else:
            c.execute('''UPDATE taskdb 
                         SET title = ?, description = ?, status = ?, createtime = ?, deadline = ?, priority = ?, category = ?
                         WHERE id = ?''',
                      (task.title, task.description,
                       task.status, task.createtime,
                       task.deadline, task.priority, task.category, task.id))
        cont.commit()
    except Exception as e:
        print(f"Ошибка при сохранении задачи: {e}")
    finally:
        if cont:
            cont.close()
    return task
def delete_task(task_id):
    cont = connection()
    try:
        c = cont.cursor()
        c.execute("DELETE FROM taskdb WHERE id = ?", (task_id,))
        cont.commit()
    except Exception as e:
        print(f"Ошибка при удалении задачи: {e}")
    finally:
        if cont:
            cont.close()
