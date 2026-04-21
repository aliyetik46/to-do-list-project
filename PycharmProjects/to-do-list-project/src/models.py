import uuid

class Task:
    def __init__(self, title, description="", category="General", priority="Medium", deadline="No Deadline", status="Pending", task_id=None):
        self.title = title
        self.category = category
        self.priority = priority # Low, Medium, High
        self.deadline = deadline
        self.status = status
        self.id = task_id if task_id else str(uuid.uuid4())

    def to_dict(self):
        return {
            "title": self.title,
            "category": self.category,
            "priority": self.priority,
            "deadline": self.deadline,
            "status": self.status,
            "id": self.id
        }