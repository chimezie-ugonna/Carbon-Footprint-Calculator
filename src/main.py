import tkinter as tk

STYLES = {
    "title": {"font": ("Arial", 20, "bold"), "fg": "#2e8b57", "bg": "#f0f0f0"},
    "label": {"font": ("Arial", 14), "bg": "#f0f0f0"},
    "button": {
        "font": ("Arial", 14),
        "width": 20,
        "height": 2,
        "fg": "white",
        "relief": "solid",
    },
    "pady": 10,
    "padx": 10,
}

class MainMenuScreen:
    def __init__(self, root):
        self.root = root

    def show(self):
        self.clear()
        self.root.title("Carbon Footprint Calculator")

        title = tk.Label(self.root, text="Welcome to the Carbon Footprint Calculator", **STYLES["title"])
        title.pack(pady=30)

        buttons = [
            ("Enter Data", self.navigate_to_data_entry),
            ("View Reports", self.navigate_to_reports),
        ]

        for text, command in buttons:
            button = tk.Button(self.root, text=text, command=command, **STYLES["button"])
            button.pack(pady=STYLES["pady"], padx=STYLES["padx"])

    def clear(self):
        """Clears all widgets from the window."""
        for widget in self.root.winfo_children():
            widget.destroy()

    def navigate_to_data_entry(self):
        """Handle navigation to the Data Entry screen."""
        print("Navigating to Data Entry screen...")

    def navigate_to_reports(self):
        """Handle navigation to the Reports screen."""
        print("Navigating to Reports screen...")


def main():
    root = tk.Tk()
    root.geometry("600x400")
    root.config(bg="#f0f0f0")

    main_menu_screen = MainMenuScreen(root)
    main_menu_screen.show()

    root.mainloop()

if __name__ == "__main__":
    main()