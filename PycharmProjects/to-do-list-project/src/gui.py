import customtkinter as ctk
from src.database import save_tasks, load_tasks
from src.models import Task


class TodoApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Advanced To-Do List - COMP1002")
        self.geometry("850x750")
        self.tasks = []

        # Başlık [cite: 21]
        ctk.CTkLabel(self, text="Advanced To-Do List", font=("Arial", 26, "bold")).pack(pady=20)

        # Giriş Paneli (Input Area)
        input_frame = ctk.CTkFrame(self)
        input_frame.pack(pady=10, padx=20, fill="x")

        self.entry = ctk.CTkEntry(input_frame, placeholder_text="Task Title", width=200)
        self.entry.grid(row=0, column=0, padx=5, pady=10)

        self.category_opt = ctk.CTkOptionMenu(input_frame, values=["General", "Work", "School", "Personal"], width=120)
        self.category_opt.grid(row=0, column=1, padx=5)

        self.priority_opt = ctk.CTkOptionMenu(input_frame, values=["Low", "Medium", "High"], width=100,
                                              fg_color="#A36A00")
        self.priority_opt.grid(row=0, column=2, padx=5)

        self.deadline_entry = ctk.CTkEntry(input_frame, placeholder_text="Deadline (e.g. 27.03)", width=120)
        self.deadline_entry.grid(row=0, column=3, padx=5)

        self.add_button = ctk.CTkButton(self, text="Add Task", command=self.add_task, width=200)
        self.add_button.pack(pady=10)

        # Kaydırılabilir Liste Alanı [cite: 30]
        self.scrollable_frame = ctk.CTkScrollableFrame(self, width=800, height=450)
        self.scrollable_frame.pack(pady=10, padx=20)

        self.load_data_at_start()

    def add_task(self):
        """Yeni görev ekler ve kalıcı olarak kaydeder[cite: 71, 73]."""
        title = self.entry.get()
        if title:
            new_task = Task(
                title=title,
                category=self.category_opt.get(),
                priority=self.priority_opt.get(),
                deadline=self.deadline_entry.get() if self.deadline_entry.get() else "No Deadline"
            )
            self.tasks.append(new_task)
            self.entry.delete(0, "end")
            self.deadline_entry.delete(0, "end")
            self.refresh_list()
            save_tasks(self.tasks)

    def delete_task(self, task_obj):
        """Görevi listeden ve veritabanından siler[cite: 71]."""
        self.tasks.remove(task_obj)
        self.refresh_list()
        save_tasks(self.tasks)

    def toggle_task(self, task_obj):
        """Görevin tamamlanma durumunu günceller[cite: 72]."""
        task_obj.status = "Completed" if task_obj.status == "Pending" else "Pending"
        self.refresh_list()
        save_tasks(self.tasks)

    def load_data_at_start(self):
        """Program açıldığında JSON'dan verileri yükler[cite: 73]."""
        saved_data = load_tasks()
        for item in saved_data:
            task = Task(
                title=item['title'],
                status=item['status'],
                category=item.get('category', 'General'),
                priority=item.get('priority', 'Medium'),
                deadline=item.get('deadline', 'No Deadline'),
                task_id=item.get('id')
            )
            self.tasks.append(task)
        self.refresh_list()

    def refresh_list(self):
        """Arayüzü temizler ve görevleri yeniden çizer[cite: 29]."""
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()

        for task in self.tasks:
            frame = ctk.CTkFrame(self.scrollable_frame)
            frame.pack(fill="x", pady=5, padx=5)

            p_color = "red" if task.priority == "High" else "orange" if task.priority == "Medium" else "gray"
            status_prefix = "✅ " if task.status == "Completed" else ""
            info_text = f"{status_prefix}{task.title} | {task.category} | Due: {task.deadline}"

            task_label = ctk.CTkLabel(frame, text=info_text, width=450, anchor="w")
            task_label.pack(side="left", padx=10)

            priority_label = ctk.CTkLabel(frame, text=task.priority, text_color=p_color, width=60)
            priority_label.pack(side="left", padx=5)

            ctk.CTkButton(frame, text="Done" if task.status == "Pending" else "Undo", width=60, fg_color="green",
                          command=lambda t=task: self.toggle_task(t)).pack(side="left", padx=5)

            ctk.CTkButton(frame, text="Delete", width=60, fg_color="red",
                          command=lambda t=task: self.delete_task(t)).pack(side="left", padx=5)