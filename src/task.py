class Task:
    def __init__(self, task_id, title, description, createtime, status="Не выполнено", deadline=None, priority=None, category=None):
        self.id = task_id
        self.title = title
        self.description = description
        self.createtime = createtime
        self.status = status
        self.deadline = deadline
        self.priority = priority
        self.category = category
    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "createtime": self.createtime,
            "status": self.status,
            "deadline": self.deadline,
            "priority": self.priority,
            "category": self.category
        }
    def __repr__(self):
        return str(self.to_dict())
    def update_status(self, new_status):
        valid_statuses = ["Не выполнено", "В процессе", "Выполнено"]
        if new_status in valid_statuses:
            self.status = new_status
        else:
            raise ValueError("Неверный статус")