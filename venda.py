from tkinter import *

class Tela_venda(Toplevel):
    def __init__(self,parent):
        super().__init__(parent)
        self.geometry("500x200")
        self.title("Vendas")
        self["bg"]= "black"