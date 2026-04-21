from src.gui import TodoApp
import customtkinter as ctk

if __name__ == "__main__":
    # Theme settings
    ctk.set_appearance_mode("System")
    ctk.set_default_color_theme("blue")

    # Start Application
    app = TodoApp()
    app.mainloop()