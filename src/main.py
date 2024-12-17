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
        frame.pack(expand=True)

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
        frame.pack(expand=True, fill="both")

        canvas = tk.Canvas(frame)
        canvas.pack(side="left", fill="both", expand=True)

        scrollbar = tk.Scrollbar(frame, orient="vertical", command=canvas.yview)
        scrollbar.pack(side="right", fill="y")

        canvas.configure(yscrollcommand=scrollbar.set)

        content_frame = tk.Frame(canvas, bg="#f0f0f0")
        canvas.create_window((0, 0), window=content_frame, anchor="nw")

        title = tk.Label(content_frame, text="Data Entry Screen", **STYLES["title"])
        title.pack(pady=30, anchor="center")

        back_button = tk.Button(content_frame, text="Back to Main Menu", command=lambda: self.navigate(MainMenuScreen), **STYLES["button"])
        back_button.pack(pady=STYLES["pady"], padx=STYLES["padx"], anchor="center")

        tk.Label(content_frame, text="Energy", font=("Arial", 16, "bold"), bg="#f0f0f0", fg="#2e8b57").pack(anchor="center", padx=STYLES["padx"], pady=STYLES["pady"])

        self.energy_bill = self.create_input_field(content_frame, "What is your average monthly electricity bill in euros?")
        self.gas_bill = self.create_input_field(content_frame, "What is your average monthly natural gas bill in euros?")
        self.fuel_bill = self.create_input_field(content_frame, "What is your average monthly fuel bill for transportation in euros?")

        tk.Label(content_frame, text="Waste", font=("Arial", 16, "bold"), bg="#f0f0f0", fg="#2e8b57").pack(anchor="center", padx=STYLES["padx"], pady=STYLES["pady"])

        self.waste_gen = self.create_input_field(content_frame, "How much waste do you generate per month in kilograms?")
        self.recycle_percentage = self.create_input_field(content_frame, "How much of that waste is recycled or composted (in percentage)?")

        tk.Label(content_frame, text="Business Travel", font=("Arial", 16, "bold"), bg="#f0f0f0", fg="#2e8b57").pack(anchor="center", padx=STYLES["padx"], pady=STYLES["pady"])

        self.km_travel = self.create_input_field(content_frame, "How many kilometers do your employees travel per year for business purposes?")
        self.fuel_efficiency = self.create_input_field(content_frame, "What is the average fuel efficiency of the vehicles used for business travel in liters per 100 kilometers?")

        button_frame = tk.Frame(content_frame, bg="#f0f0f0")
        button_frame.pack(pady=STYLES["pady"])

        calculate_button = tk.Button(button_frame, text="Calculate", **STYLES["button"])
        calculate_button.pack(side="left", padx=STYLES["padx"])

        generate_button = tk.Button(button_frame, text="Generate PDF", **STYLES["button"])
        generate_button.pack(side="left", padx=STYLES["padx"])

        content_frame.update_idletasks()
        canvas.config(scrollregion=canvas.bbox("all"))

    def validate_numeric_input(self, input_value):
        if input_value == "":
            return True
        try:
            float(input_value)
            return True
        except ValueError:
            return False

    def create_input_field(self, frame, question):
        label = tk.Label(frame, text=question, **STYLES["label"])
        label.pack(anchor="center", padx=STYLES["padx"], pady=STYLES["pady"])

        validate = lambda input_value: self.validate_numeric_input(input_value)
        entry = tk.Entry(frame, validate="key", validatecommand=(frame.register(validate), "%P"))
        entry.pack(padx=STYLES["padx"], pady=STYLES["pady"])

        return entry

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
    root.geometry("600x600")
    root.config(bg="#f0f0f0")
    root.resizable(True, True)

    def navigate(screen_class):
        screen_class(root, navigate).show()

    main_menu_screen = MainMenuScreen(root, navigate)
    main_menu_screen.show()

    root.mainloop()

if __name__ == "__main__":
    main()