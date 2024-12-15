import tkinter as tk
from tkinter import ttk

STYLES = {
    "title": {"font": ("Arial", 20, "bold"), "fg": "#2e8b57", "bg": "#f0f0f0"},
    "label": {"font": ("Arial", 14), "bg": "#f0f0f0"},
    "button": {
        "font": ("Arial", 14),
        "width": 20,
        "height": 2,
        "fg": "black",
        "relief": "solid",
    },
    "pady": 10,
    "padx": 10,
}

class MainMenuScreen:
    def __init__(self, root, navigate):
        self.root = root
        self.navigate = navigate

    def show(self):
        self.clear()
        self.root.title("Carbon Footprint Calculator")

        frame = tk.Frame(self.root, bg="#f0f0f0")
        frame.pack(expand=True, fill='both')

        title_label = tk.Label(frame, text="Welcome to the Carbon Footprint Calculator", **STYLES["title"])
        title_label.pack(pady=30, anchor="center")

        buttons = [
            ("Enter Data", lambda: self.navigate(DataEntryScreen)),
            ("View Reports", lambda: self.navigate(ReportsScreen)),
        ]
        for text, command in buttons:
            button = tk.Button(frame, text=text, command=command, **STYLES["button"])
            button.pack(pady=STYLES["pady"], padx=STYLES["padx"], anchor="center")

    def clear(self):
        for widget in self.root.winfo_children():
            widget.destroy()

class DataEntryScreen:
    def __init__(self, root, navigate):
        self.root = root
        self.navigate = navigate

    def show(self):
        self.clear()
        self.root.title("Data Entry")

        frame = tk.Frame(self.root, bg="#f0f0f0")
        frame.pack(expand=True, fill='both')

        title = tk.Label(frame, text="Data Entry Screen", **STYLES["title"])
        title.pack(pady=30, anchor="center")

        back_button = tk.Button(frame, text="Back to Main Menu", command=lambda: self.navigate(MainMenuScreen), **STYLES["button"])
        back_button.pack(pady=STYLES["pady"], padx=STYLES["padx"], anchor="center")

        notebook = ttk.Notebook(frame)
        notebook.pack(expand=True, fill="both", padx=STYLES["padx"], pady=STYLES["pady"])

        energy_tab = ttk.Frame(notebook)
        notebook.add(energy_tab, text="Energy")
        energy_label = tk.Label(energy_tab, text="Energy-related questions here", **STYLES["label"])
        energy_label.pack(padx=STYLES["padx"], pady=STYLES["pady"])

        waste_tab = ttk.Frame(notebook)
        notebook.add(waste_tab, text="Waste")
        waste_label = tk.Label(waste_tab, text="Waste-related questions here", **STYLES["label"])
        waste_label.pack(padx=STYLES["padx"], pady=STYLES["pady"])

        business_travel_tab = ttk.Frame(notebook)
        notebook.add(business_travel_tab, text="Business Travel")
        business_travel_label = tk.Label(business_travel_tab, text="Business Travel-related questions here", **STYLES["label"])
        business_travel_label.pack(padx=STYLES["padx"], pady=STYLES["pady"])

    def clear(self):
        for widget in self.root.winfo_children():
            widget.destroy()

class ReportsScreen:
    def __init__(self, root, navigate):
        self.root = root
        self.navigate = navigate

    def show(self):
        self.clear()
        self.root.title("View Reports")

        frame = tk.Frame(self.root, bg="#f0f0f0")
        frame.pack(expand=True, fill='both')

        title = tk.Label(frame, text="Reports Screen", **STYLES["title"])
        title.pack(pady=30, anchor="center")

        back_button = tk.Button(frame, text="Back to Main Menu", command=lambda: self.navigate(MainMenuScreen), **STYLES["button"])
        back_button.pack(pady=STYLES["pady"], padx=STYLES["padx"], anchor="center")

    def clear(self):
        for widget in self.root.winfo_children():
            widget.destroy()

def main():
    root = tk.Tk()
    root.geometry("600x400")
    root.config(bg="#f0f0f0")
    root.resizable(True, True)

    def navigate(screen_class):
        screen_class(root, navigate).show()

    main_menu_screen = MainMenuScreen(root, navigate)
    main_menu_screen.show()

    root.mainloop()

if __name__ == "__main__":
    main()