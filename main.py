from customtkinter import CTk, CTkLabel
from tkinter import Menu
from interface.show_grafics import ShowGrafics
from interface.show_grafics_interval import ShowGraficsInterval
from interface.show_grafics_equations import ShowGraficsWithEquations
from interface.chat import ChatApp
from interface.calculator import CalculatorApp

class Main:
    def __init__(self):
        self.root = CTk()
        self.root.title("Fisica con Abel")
        self.root.geometry("300x300")
        self.root.resizable(False, False)
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.config(menu=self.create_menu())

        self.label = CTkLabel(self.root, text="Fisica con Abel", font=("Arial", 20))
        self.label.pack()
        self.root.mainloop()
    
    def create_menu(self):
        menu = Menu(self.root)
        cinematica_menu = Menu(menu, tearoff=0)
        cinematica_menu.add_command(label="Generar Graficas", command=self.generar_graficas)
        cinematica_menu.add_command(label="Generar Graficas y Ecuaciones", command=self.generar_graficas_y_ecuaciones)
        cinematica_menu.add_command(label="Generar Graficas con intervalos", command=self.generar_graficas_con_intervalos)
        cinematica_menu.add_separator()
        cinematica_menu.add_command(label="Exit", command=self.on_closing)
        menu.add_cascade(label="Cinematica", menu=cinematica_menu)
        chat_menu = Menu(menu, tearoff=0)
        chat_menu.add_command(label="Chat", command=self.chat)
        chat_menu.add_separator()
        chat_menu.add_command(label="Exit", command=self.on_closing)
        menu.add_cascade(label="Chat", menu=chat_menu)
        calculadora_menu = Menu(menu, tearoff=0)
        calculadora_menu.add_command(label="Calculadora", command=self.calculadora)
        calculadora_menu.add_separator()
        calculadora_menu.add_command(label="Exit", command=self.on_closing)
        menu.add_cascade(label="Calculadora", menu=calculadora_menu)
        return menu
    
    def on_closing(self):
        self.root.destroy()
    
    def generar_graficas(self):
        ShowGrafics()

    def generar_graficas_y_ecuaciones(self):
        ShowGraficsWithEquations()

    def generar_graficas_con_intervalos(self):
        ShowGraficsInterval()
    
    def chat(self):
        ChatApp()

    def calculadora(self):
        CalculatorApp()

if __name__ == "__main__":
    Main()