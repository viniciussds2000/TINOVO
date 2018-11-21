from tkinter import *

class Patio_1(Tk):
    def __init__(self):
        super().__init__()

        self["bg"] = "beige"
        self.geometry("400x400")
        self.title("Concessionaria TINOVO ")

        bt = Button(self, width=10, height=3, text="UNO")
        bt2 = Button(self, width=10, height=3, text="Hilux")
        bt3 = Button(self, width=10, height=3, text="UP")
        bt4 = Button(self, width=10, height=3, text="KA")
        bt5 = Button(self, width=10, height=3, text="CORSA")


        bt.place(x=50, y=50)
        bt2.place(x=150, y=50)
        bt3.place(x=250, y=50)
        bt4.place(x=50, y=150)
        bt5.place(x=150, y=150)

'''
    def btn_click(self):
        open(Tela_venda())
class Tela_Venda():
'''
