import json
import os

DATA_FILE = "data/tasks.json"

def save_tasks(tasks_list):
    """Saves the current task list to a JSON file."""
    if not os.path.exists("data"):
        os.makedirs("data")
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump([task.to_dict() for task in tasks_list], f, indent=4)

def load_tasks():
    """Loads tasks from the JSON file if it exists."""
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return []