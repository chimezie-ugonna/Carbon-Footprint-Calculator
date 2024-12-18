import tkinter as tk
from calculations import calculate_energy_footprint, calculate_waste_footprint, calculate_business_travel_footprint
from ai import generate_report
from tkinter import messagebox
from pdf_generator import generate_pdf
import threading

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
        title_label.pack(pady=STYLES["pady"], anchor="center")

        description_text = (
            "AI-powered carbon footprint calculator providing actionable insights to reduce energy, waste, and business travel emissions."
        )
        description_label = tk.Label(frame, text=description_text, font=("Arial", 12), bg="#f0f0f0", wraplength=500)
        description_label.pack(pady=STYLES["pady"], padx=STYLES["padx"], anchor="center")

        proceed_button = tk.Button(frame, text="Proceed", command=lambda: self.navigate(DataEntryScreen), **STYLES["button"])
        proceed_button.pack(pady=STYLES["pady"], padx=STYLES["padx"], anchor="center")

    def clear(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        self.root.update()

class DataEntryScreen:
    def __init__(self, root, navigate):
        self.root = root
        self.navigate = navigate
        self.calculate_button = None
        self.task_done_event = threading.Event()
        self.report = ""
        self.energy_footprint = 0
        self.waste_footprint = 0
        self.business_travel_footprint = 0

    def show(self):
        self.clear()

        self.root.title("Data Entry")

        frame = tk.Frame(self.root, bg="#f0f0f0")
        frame.pack(expand=True, fill="both")

        canvas = tk.Canvas(frame)
        canvas.pack(side="left", fill="both", expand=True)

        v_scrollbar = tk.Scrollbar(frame, orient="vertical", command=canvas.yview)
        v_scrollbar.pack(side="right", fill="y")

        h_scrollbar = tk.Scrollbar(frame, orient="horizontal", command=canvas.xview)
        h_scrollbar.pack(side="bottom", fill="x")

        canvas.configure(yscrollcommand=v_scrollbar.set, xscrollcommand=h_scrollbar.set)

        content_frame = tk.Frame(canvas, bg="#f0f0f0")
        self.content_frame_window = canvas.create_window((0, 0), window=content_frame, anchor="nw")

        tk.Label(content_frame, text="Data Entry Screen", **STYLES["title"]).pack(
            pady=STYLES["pady"], anchor="center"
        )

        tk.Button(content_frame, text="Back to Main Menu", 
                  command=lambda: self.navigate(MainMenuScreen), 
                  **STYLES["button"]).pack(pady=STYLES["pady"], padx=STYLES["padx"], anchor="center")

        self.create_section(content_frame, "Energy", [
            ("What is your average monthly electricity bill in euros?", "energy_bill"),
            ("What is your average monthly natural gas bill in euros?", "gas_bill"),
            ("What is your average monthly fuel bill for transportation in euros?", "fuel_bill"),
        ])

        self.create_section(content_frame, "Waste", [
            ("How much waste do you generate per month in kilograms?", "waste_gen"),
            ("How much of that waste is recycled or composted (in percentage)?", "recycle_percentage"),
        ])

        self.create_section(content_frame, "Business Travel", [
            ("How many kilometers do your employees travel per year for business purposes?", "km_travel"),
            ("What is the average fuel efficiency of the vehicles used (liters per 100 km)?", "fuel_efficiency"),
        ])

        button_frame = tk.Frame(content_frame, bg="#f0f0f0")
        button_frame.pack(pady=STYLES["pady"])

        self.calculate_button = tk.Button(
            button_frame, text="Compute", command=self.on_calculate, **STYLES["button"]
        )
        self.calculate_button.pack(side="left", padx=STYLES["padx"])

        tk.Button(button_frame, text="Generate PDF", 
                  command=lambda: generate_pdf(self.response_text.get(1.0, tk.END), self.energy_footprint, self.waste_footprint, self.business_travel_footprint, self.root), 
                  **STYLES["button"]).pack(side="left", padx=STYLES["padx"])

        self.response_text = tk.Text(content_frame, wrap="word", font=("Arial", 12), state=tk.DISABLED)
        self.response_text.pack(fill="both", expand=True, padx=STYLES["padx"], pady=STYLES["pady"])

        self.bind_resize_events(canvas, content_frame)

    def bind_resize_events(self, canvas, content_frame):
        def update_scroll_region(event=None):
            canvas.configure(scrollregion=canvas.bbox("all"))

        def bind_canvas_width(event=None):
            canvas.itemconfig(self.content_frame_window, width=canvas.winfo_width())
            canvas.configure(scrollregion=canvas.bbox("all"))

        content_frame.bind("<Configure>", update_scroll_region)
        canvas.bind("<Configure>", bind_canvas_width)

    def create_section(self, parent, title, fields):
        tk.Label(parent, text=title, font=("Arial", 16, "bold"), bg="#f0f0f0", fg="#2e8b57").pack(
            anchor="center", padx=STYLES["padx"], pady=STYLES["pady"]
        )
        for question, attr in fields:
            setattr(self, attr, self.create_input_field(parent, question))

    def create_input_field(self, parent, question):
        tk.Label(parent, text=question, **STYLES["label"]).pack(
            anchor="center", padx=STYLES["padx"], pady=STYLES["pady"]
        )
        validate = lambda val: self.validate_numeric_input(val)
        entry = tk.Entry(parent, validate="key", validatecommand=(parent.register(validate), "%P"))
        entry.pack(padx=STYLES["padx"], pady=STYLES["pady"])
        return entry

    def validate_numeric_input(self, input_value):
        if input_value == "":
            return True
        try:
            float(input_value)
            return True
        except ValueError:
            return False

    def on_calculate(self):
        if not self.check_empty_fields():
            messagebox.showwarning("Input Error", "Please fill in all the fields first.")
            return

        self.task_done_event.clear()
        self.calculate_button.config(state=tk.DISABLED, text="Computing...")

        threading.Thread(target=self.calculate_footprints).start()
        self.check_task_status()

    def check_empty_fields(self):
        fields = [
            self.energy_bill, self.gas_bill, self.fuel_bill,
            self.waste_gen, self.recycle_percentage,
            self.km_travel, self.fuel_efficiency
        ]
        return all(field.get().strip() for field in fields)

    def calculate_footprints(self):
        try:
            self.energy_footprint = calculate_energy_footprint(
                float(self.energy_bill.get()), float(self.gas_bill.get()), float(self.fuel_bill.get())
            )
            self.waste_footprint = calculate_waste_footprint(
                float(self.waste_gen.get()), float(self.recycle_percentage.get())
            )
            self.business_travel_footprint = calculate_business_travel_footprint(
                float(self.km_travel.get()), float(self.fuel_efficiency.get())
            )
            self.report = generate_report(self.energy_footprint, self.waste_footprint, self.business_travel_footprint)
        except Exception as e:
            self.report = f"Error: {e}"
        finally:
            self.task_done_event.set()

    def check_task_status(self):
        if self.task_done_event.is_set():
            self.update_response(self.report)
        else:
            self.root.after(100, self.check_task_status)

    def update_response(self, report):
        self.response_text.config(state=tk.NORMAL)
        self.response_text.delete(1.0, tk.END)
        self.response_text.insert(tk.END, report)
        self.response_text.config(state=tk.DISABLED)
        self.calculate_button.config(state=tk.NORMAL, text="Compute")

    def clear(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        self.root.update()
                
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