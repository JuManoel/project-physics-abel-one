from customtkinter import CTk, CTkLabel,CTkEntry,CTkButton
from tkinter import Menu
from build.grafic import Grafic

class ShowGrafics:
    def __init__(self):
        self.root = CTk()
        self.root.title("Graficas")
        self.root.geometry("300x300")
        self.root.resizable(False, False)
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.config(menu=self.create_menu())
        self.label = CTkLabel(self.root, text="Graficas de Cinematica", font=("Arial", 20))
        self.label.pack()

        self.acceleration_label = CTkLabel(self.root, text="Aceleración Inicial:")
        self.acceleration_label.pack()
        self.acceleration_entry = CTkEntry(self.root)
        self.acceleration_entry.insert(0, "0")
        self.acceleration_entry.pack()

        self.velocity_label = CTkLabel(self.root, text="Velocidad Inicial:")
        self.velocity_label.pack()
        self.velocity_entry = CTkEntry(self.root)
        self.velocity_entry.insert(0, "0")
        self.velocity_entry.pack()

        self.position_label = CTkLabel(self.root, text="Posición Inicial:")
        self.position_label.pack()
        self.position_entry = CTkEntry(self.root)
        self.position_entry.insert(0, "0")
        self.position_entry.pack()

        self.button = CTkButton(self.root, text="Generar Grafica", command=self.generarGrafica)
        self.button.pack()

        self.root.mainloop()
    
    def create_menu(self):
        menu = Menu(self.root)
        file_menu = Menu(menu, tearoff=0)
        file_menu.add_command(label="Exit", command=self.on_closing)
        menu.add_cascade(label="Cinematica", menu=file_menu)
        return menu


    def generarGrafica(self):
        a = float(self.acceleration_entry.get())
        v = float(self.velocity_entry.get())
        p = float(self.position_entry.get())
        Grafic(a, v, p)
        
    def on_closing(self):
        self.root.destroy()