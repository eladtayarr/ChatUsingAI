from tkinter import Tk
from chat_window import ChatWindow

class ChatApp:
    def __init__(self):
        self.root = Tk()
        self.root.geometry("400x500")  # Set the window size
        self.chat_window = ChatWindow(self.root)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = ChatApp()
    app.run()