#  TaskMaster Pro: Advanced To-Do List Application

[cite_start]**TaskMaster Pro** is a high-performance desktop application developed as part of the **COMP1002 - Advanced Python** course[cite: 4, 33]. [cite_start]This project showcases advanced programming concepts such as Object-Oriented Programming (OOP), modular architecture, and persistent data management[cite: 27, 28].

##  Team Members
* [cite_start]**Mehmet Ali Yetik** - 212010020091 [cite: 8]
* [cite_start]**Yusuf Kart** - 212010020115 [cite: 7]

##  Key Features
* [cite_start]**Full Task Management:** Create, track, and delete tasks with ease[cite: 14].
* [cite_start]**Status Tracking:** Toggle between "Pending" and "Completed" status with visual indicators[cite: 15].
* [cite_start]**Advanced Metadata:** Assign **Categories** (Work, School, Personal), **Priority Levels** (Low, Medium, High), and **Deadlines** to every task[cite: 17, 52].
* [cite_start]**Persistent Storage:** Tasks are automatically saved to a `JSON` database, ensuring no data is lost between sessions[cite: 16, 23].
* [cite_start]**Modern GUI:** Built with `CustomTkinter` for a sleek, responsive, and dark-mode friendly desktop experience[cite: 6, 22].

##  Project Structure (Modular Design)
[cite_start]The project follows a clean-code modular structure to ensure maintainability[cite: 27, 29]:
* `main.py`: The entry point of the application.
* [cite_start]`src/gui.py`: Manages the entire User Interface and event handling[cite: 22].
* [cite_start]`src/models.py`: Defines the `Task` class (OOP principles)[cite: 28].
* [cite_start]`src/database.py`: Handles file I/O and JSON data persistence[cite: 23].
* `data/tasks.json`: The storage file for user data.

## 🛠️ Technical Stack
* [cite_start]**Language:** Python 3.x [cite: 21]
* [cite_start]**Library:** CustomTkinter (Advanced GUI) [cite: 22]
* [cite_start]**Storage:** JSON (Structured Data Persistence) [cite: 23]
* [cite_start]**Version Control:** Git & GitHub [cite: 24, 25]

##  Installation & Running
1. **Clone the repository:**
   ```bash
   git clone [https://github.com/aliyetik46/to-do-list-project.git](https://github.com/aliyetik46/to-do-list-project.git)
