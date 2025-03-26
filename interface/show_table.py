from customtkinter import CTk, CTkLabel,CTkEntry,CTkButton
from tkinter import Menu
from build.table import Table
from .message_box_error import show_error
class ShowTableInterval:
    def __init__(self):
        self.root = CTk()
        self.root.title("Tabla")
        self.root.geometry("300x400")
        self.root.resizable(False, False)
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.config(menu=self.create_menu())
        self.label = CTkLabel(self.root, text="Tabla de Cinematica", font=("Arial", 20))
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

        self.tiempo_inical_label = CTkLabel(self.root, text="Tiempo Inicial:")
        self.tiempo_inical_label.pack()
        self.tiempo_inical_entry = CTkEntry(self.root)
        self.tiempo_inical_entry.insert(0, "0")
        self.tiempo_inical_entry.pack()

        self.tiempo_final_label = CTkLabel(self.root, text="Tiempo Final:")
        self.tiempo_final_label.pack()
        self.tiempo_final_entry = CTkEntry(self.root)
        self.tiempo_final_entry.insert(0, "0")
        self.tiempo_final_entry.pack()

        self.button = CTkButton(self.root, text="Generar Tabla", command=self.generarTabla)
        self.button.pack()

        self.root.mainloop()
    
    def create_menu(self):
        menu = Menu(self.root)
        file_menu = Menu(menu, tearoff=0)
        file_menu.add_command(label="Exit", command=self.on_closing)
        menu.add_cascade(label="Cinematica", menu=file_menu)
        return menu
    
    def on_closing(self):
        self.root.destroy()


    def generarTabla(self):
        try:
            a = float(self.acceleration_entry.get())
            v = float(self.velocity_entry.get())
            p = float(self.position_entry.get())
            t_i = float(self.tiempo_inical_entry.get())
            t_f = float(self.tiempo_final_entry.get())
            if t_i >= t_f:
                show_error("El tiempo inicial debe ser menor al tiempo final")
                return
            Table(a, v, p, (t_i, t_f))
        except ValueError:
            show_error("Por favor ingrese valores validos")
            return
        except Exception as e:
            show_error(str(e))
        
    def on_closing(self):
        self.root.destroy()