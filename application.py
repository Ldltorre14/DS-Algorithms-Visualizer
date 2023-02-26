from customtkinter import *
from customtkinter import CTkBaseClass
from tkinter import *
from tkinter import messagebox
import tkinter.ttk as ttk
import random
from PIL import Image, ImageTk
import time


class application(CTk):
    def __init__(self):
        super().__init__()
        self.geometry("920x600")
        self.title("DS&A Visualizer")
        self.config(bg="black")
        self.resizable(False,False)
        self.label()
        self.canvas()
        self.bubblesort(data=[i for i in random.sample(range(1000),1000)])
        self.mainloop()
        
    
    def label(self):
        #Background Image setting
        self.Image = Image.open("Resources/bg.jpg")
        self.resizedImage = self.Image.resize((925,605))
        self.backgroundImage = ImageTk.PhotoImage(self.resizedImage)
        self.backgroundImageLabel = Label(self,image=self.backgroundImage)
        self.backgroundImageLabel.place(x=-5,y=0)
    
    
    
    def canvas(self):
        self.visualizer = CTkCanvas(self,width=875,height=350)
        self.visualizer.place(x=20,y=10)
    
    
    def draw(self,data):
        self.visualizer.delete("all")
        visualizerHeight = 350
        visualizerWidth = 875
        bar_width = visualizerWidth/(len(data))
        bar_height_unit = visualizerHeight / max(data)
        offset = 2
 
        for i, height in enumerate(data):
            # top left corner
            x0 = i*bar_width + offset
            y0 = visualizerHeight - (bar_height_unit * height)
 
            # bottom right corner
            x1 = ((i+1)*bar_width) + offset
            y1 = visualizerHeight
 
            self.visualizer.create_rectangle(x0, y0, x1, y1, fill="orange")
            #self.visualizer.create_text(x0 + bar_width/2, y1 - 10, text=str(data[i]))
        
            
    
    def bubblesort(self, data):
        n = len(data)
        for i in range(n):
            self.draw(data)
            self.update()
            time.sleep(0.01)
            for j in range(n - i - 1):
                if data[j] > data[j + 1]:
                    data[j], data[j + 1] = data[j + 1], data[j]

                    # Call draw() method and update the window
                    
                    #time.sleep(0.00000001)
                    
        
        
        

    
                

