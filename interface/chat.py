from customtkinter import CTk, CTkLabel,CTkEntry,CTkButton, CTkFrame, CTkTextbox, CTkScrollbar
from tkinter import Menu
from tkinter import messagebox
from api.gemini import GeminiAPI
from .message_box_error import show_error

class ChatApp:
    def __init__(self):
        try:
            self.api = GeminiAPI()            
        except Exception as e:
            show_error("Problema al cargar el modelo de Gemini")
            return   
        self.root = CTk()
        self.root.title("Chat")
        self.root.geometry("300x300")
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.config(menu=self.create_menu())

        self.label = CTkLabel(self.root, text="Chat", font=("Arial", 20))
        self.label.pack()
        
        self.entry = CTkEntry(self.root)
        self.entry.pack()
        
        self.button = CTkButton(self.root,text="Enviar",command=self.send_message)
        self.button.pack()
        
        self.chat_frame = CTkFrame(self.root)
        self.chat_frame.pack(fill="both", expand=True)
        
        self.chat_text = CTkTextbox(self.chat_frame, wrap="word")
        self.chat_text.pack(side="left", fill="both", expand=True)
        
        self.scrollbar = CTkScrollbar(self.chat_frame, command=self.chat_text.yview)
        self.scrollbar.pack(side="right", fill="y")
        
        self.chat_text.configure(yscrollcommand=self.scrollbar.set)

        self.root.mainloop()
    
    def create_menu(self):
        menu = Menu(self.root)
        file_menu = Menu(menu, tearoff=0)
        file_menu.add_command(label="Exit", command=self.on_closing)
        menu.add_cascade(label="Chat", menu=file_menu)
        return menu

    def on_closing(self):
        self.root.destroy()
    
    def send_message(self):
        text = self.entry.get()
        out = self.api.generate_response(text)
        self.chat_text.insert("end", f"User: {text}\n")
        self.chat_text.insert("end", f"Bot: {out}\n")
        self.entry.delete(0, "end")
    
        
