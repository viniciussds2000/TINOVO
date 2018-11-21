from tkinter import *

class Patio_1(Tk):
    def __init__(self):
        super().__init__()

        self["bg"] = "beige"
        self.geometry("400x400")
        self.title("Concessionaria TINOVO ")

        self.bt = Button(self, width=10, height=3, text="UNO")
        self.bt2 = Button(self, width=10, height=3, text="Hilux")
        self.bt3 = Button(self, width=10, height=3, text="UP")
        self.bt4 = Button(self, width=10, height=3, text="KA")
        self.bt5 = Button(self, width=10, height=3, text="CORSA")

        self.bt.place(x=50, y=50)
        self.bt2.place(x=150, y=50)
        self.bt3.place(x=250, y=50)
        self.bt4.place(x=50, y=150)
        self.bt5.place(x=150, y=150)

'''     


    
    def btn_click(self):
        open(Tela_venda())
class Tela_Venda():
'''
