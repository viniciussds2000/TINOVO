from tkinter import *
from venda import Tela_venda

class Patio_1(Tk):
    def __init__(self):
        super().__init__()

        self["bg"] = "beige"
        self.geometry("400x400")
        self.title("Concessionaria TINOVO ")

        self.bt = Button(self, width=10, height=3, text="UNO", command=self.btn_venda)
        self.bt2 = Button(self, width=10, height=3, text="Hilux")
        self.bt3 = Button(self, width=10, height=3, text="UP")
        self.bt4 = Button(self, width=10, height=3, text="KA")
        self.bt5 = Button(self, width=10, height=3, text="CORSA")

        self.bt.grid(row=1,column=1)
        self.bt2.grid(row=1,column=2)
        self.bt3.grid(row=1,column=3)
        self.bt4.grid(row=2,column=1)
        self.bt5.grid(row=2,column=2)

    def btn_venda(self):
        Tela_venda(self)



