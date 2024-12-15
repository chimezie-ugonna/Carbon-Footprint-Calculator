import tkinter as tk

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
    def __init__(self, root):
        self.root = root
        self.title_label = None

    def show(self):
        self.clear()
        self.root.title("Carbon Footprint Calculator")

        frame = tk.Frame(self.root, bg="#f0f0f0")
        frame.pack(expand=True)

        self.title_label = tk.Label(frame, text="Welcome to the Carbon Footprint Calculator", **STYLES["title"])
        self.title_label.pack(pady=30, anchor="center")

        self.update_wraplength()

        buttons = [
            ("Enter Data", self.navigate_to_data_entry),
            ("View Reports", self.navigate_to_reports),
        ]
        for text, command in buttons:
            button = tk.Button(frame, text=text, command=command, **STYLES["button"])
            button.pack(pady=STYLES["pady"], padx=STYLES["padx"], anchor="center")

        self.root.bind("<Configure>", self.update_wraplength)

    def update_wraplength(self, event=None):
        window_width = self.root.winfo_width()
        self.title_label.config(wraplength=window_width - 40)

    def clear(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def navigate_to_data_entry(self):
        data_entry_screen = DataEntryScreen(self.root, self.show)
        data_entry_screen.show()

    def navigate_to_reports(self):
        reports_screen = ReportsScreen(self.root, self.show)
        reports_screen.show()


class DataEntryScreen:
    def __init__(self, root, back_function):
        self.root = root
        self.back_function = back_function

    def show(self):
        self.clear()
        self.root.title("Data Entry")

        frame = tk.Frame(self.root, bg="#f0f0f0")
        frame.pack(expand=True)

        title = tk.Label(frame, text="Data Entry Screen", **STYLES["title"])
        title.pack(pady=30, anchor="center")

        back_button = tk.Button(frame, text="Back to Main Menu", command=self.back_function, **STYLES["button"])
        back_button.pack(pady=STYLES["pady"], padx=STYLES["padx"], anchor="center")

    def clear(self):
        for widget in self.root.winfo_children():
            widget.destroy()


class ReportsScreen:
    def __init__(self, root, back_function):
        self.root = root
        self.back_function = back_function

    def show(self):
        self.clear()
        self.root.title("View Reports")

        frame = tk.Frame(self.root, bg="#f0f0f0")
        frame.pack(expand=True)

        title = tk.Label(frame, text="Reports Screen", **STYLES["title"])
        title.pack(pady=30, anchor="center")

        back_button = tk.Button(frame, text="Back to Main Menu", command=self.back_function, **STYLES["button"])
        back_button.pack(pady=STYLES["pady"], padx=STYLES["padx"], anchor="center")

    def clear(self):
        for widget in self.root.winfo_children():
            widget.destroy()


def main():
    root = tk.Tk()
    root.geometry("600x400")
    root.config(bg="#f0f0f0")
    root.resizable(True, True)

    main_menu_screen = MainMenuScreen(root)
    main_menu_screen.show()

    root.mainloop()


if __name__ == "__main__":
    main()