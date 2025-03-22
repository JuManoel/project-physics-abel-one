from customtkinter import CTk, CTkLabel, CTkEntry, CTkButton, CTkFrame, CTkTextbox, CTkScrollbar
from tkinter import Menu
from sympy import symbols, diff, integrate, Eq, solve

class CalculatorApp:
    def __init__(self):
        self.root = CTk()
        self.root.title("Calculadora")
        self.root.geometry("400x400")
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.config(menu=self.create_menu())

        self.label = CTkLabel(self.root, text="Calculadora", font=("Arial", 20))
        self.label.pack()

        self.entry = CTkEntry(self.root)
        self.entry.pack()

        self.button_frame = CTkFrame(self.root)
        self.button_frame.pack()

        self.calc_button = CTkButton(self.button_frame, text="Calcular", command=self.calculate)
        self.calc_button.grid(row=0, column=0, padx=5, pady=5)

        self.deriv_button = CTkButton(self.button_frame, text="Derivada", command=self.calculate_derivative)
        self.deriv_button.grid(row=0, column=1, padx=5, pady=5)

        self.integ_button = CTkButton(self.button_frame, text="Integral", command=self.calculate_integral)
        self.integ_button.grid(row=0, column=2, padx=5, pady=5)

        self.result_text = CTkTextbox(self.root, wrap="word", height=10)
        self.result_text.pack(fill="both", expand=True)

        self.scrollbar = CTkScrollbar(self.result_text, command=self.result_text.yview)
        self.scrollbar.grid(row=0, column=1, sticky="ns")
        self.result_text.configure(yscrollcommand=self.scrollbar.set)

        self.root.mainloop()

    def create_menu(self):
        menu = Menu(self.root)
        file_menu = Menu(menu, tearoff=0)
        file_menu.add_command(label="Exit", command=self.on_closing)
        menu.add_cascade(label="Archivo", menu=file_menu)
        return menu

    def on_closing(self):
        self.root.destroy()

    def calculate(self):
        expr = self.entry.get()
        try:
            x = symbols('x')
            if "x" not in expr:
                result = eval(expr)
                self.result_text.insert("end", f"{expr} = {result}\n")
            else:
                result =solve(Eq(eval(expr), 0), x)
                self.result_text.insert("end", f"{expr} = {result[0] if len(result) == 1 else result}\n")
        except Exception as e:
            self.result_text.insert("end", f"Error: {e}\n")

    def calculate_derivative(self):
        expr = self.entry.get()
        try:
            x = symbols('x')
            result = diff(eval(expr), x)
            self.result_text.insert("end", f"Derivada: {result}\n")
        except Exception as e:
            self.result_text.insert("end", f"Error: {e}\n")

    def calculate_integral(self):
        expr = self.entry.get()
        try:
            x = symbols('x')
            result = integrate(eval(expr), x)
            self.result_text.insert("end", f"Integral: {result}\n")
        except Exception as e:
            self.result_text.insert("end", f"Error: {e}\n")
