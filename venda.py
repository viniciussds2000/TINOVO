from tkinter import *

class Tela_venda(Toplevel):
    def __init__(self,parent):
        super().__init__(parent)
        self.geometry("500x200")
        self.title("Vendas")
        self.transient(parent)
        self.grab_set()
        self.cad1=Label(self,text="Comprador: ")
        self.cad1.place(x=5,y=6)
        self.cad1ed=Entry()
        self.cad1ed.place(x=7,y=6)