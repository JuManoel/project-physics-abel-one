from customtkinter import CTk, CTkLabel
from tkinter import Menu
import tkinter.ttk as ttk
import tksheet
class Table:
    def __init__(self, a, v, p, interval: tuple[float, float] = (0, 10)):
        self.interval = interval
        self.t = [i/20 for i in range(int(interval[0]*20), int(interval[1]*20)+1)]
        self.ya = [a for _ in self.t]
        self.yv = [v + a*i for i in self.t]
        self.yp = [p + v*i + 0.5*a*i**2 for i in self.t]
        self.values = [[f'{self.t[i]:.2f}', f'{self.ya[i]:.2f}', f'{self.yv[i]:.2f}', f'{self.yp[i]:.2f}'] for i in range(len(self.t))]
        self.show_table()
    
    def show_table(self):
        self.root = CTk()
        self.root.title("Tabla")
        self.root.geometry("500x500")
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.config(menu=self.create_menu())
        self.label = CTkLabel(self.root, text="Tabla de Cinematica", font=("Arial", 20))
        self.label.pack()

        frame = ttk.Frame(self.root)
        frame.pack(expand=True, fill='both', padx=20, pady=20)

        self.table = tksheet.Sheet(frame, headers=['Tiempo', 'Aceleración', 'Velocidad', 'Posición'])
        self.table.set_sheet_data(self.values)
        self.table.pack(expand=True, fill='both')
        self.table.enable_bindings('all')
        self.table.disable_bindings(['rc_insert_column', 'rc_delete_column', 'edit_cell', 'delete', 'paste', 'cut', 'rc_delete_row', 'rc_insert_row'])

        self.root.mainloop() 

    def create_menu(self):
        menu = Menu(self.root)
        file_menu = Menu(menu, tearoff=0)
        file_menu.add_command(label="Exit", command=self.on_closing)
        menu.add_cascade(label="Cinematica", menu=file_menu)
        return menu

    def on_closing(self):
        self.root.destroy()