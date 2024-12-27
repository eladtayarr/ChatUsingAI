from tkinter import Frame, Text, Scrollbar, VERTICAL, END, Entry, Button
from ai_connection import AIConnection

class ChatWindow(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()
        self.ai_connection = AIConnection()

    def create_widgets(self):
        self.text_area = Text(self, wrap='word', state='disabled')
        self.text_area.pack(expand=True, fill='both')

        self.scrollbar = Scrollbar(self, orient=VERTICAL, command=self.text_area.yview)
        self.scrollbar.pack(side='right', fill='y')

        self.text_area['yscrollcommand'] = self.scrollbar.set

        self.entry = Entry(self)
        self.entry.pack(fill='x')
        self.entry.bind("<Return>", self.send_message)

        self.send_button = Button(self, text="Send", command=self.send_message)
        self.send_button.pack()

    def send_message(self, event=None):
        user_message = self.entry.get()
        self.display_message("You: " + user_message)
        self.entry.delete(0, END)
        
        response = self.ai_connection.send_message(user_message)
        self.display_message("AI: " + response)

    def display_message(self, message):
        self.text_area.config(state='normal')
        self.text_area.insert(END, message + '\n')
        self.text_area.config(state='disabled')
        self.text_area.yview(END)