import customtkinter



class application(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("920x600")
        self.resizable(False,False)
    
    def label(self):
        print("hello")
