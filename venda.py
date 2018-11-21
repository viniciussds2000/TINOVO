from tkinter import *

class Tela_venda(Toplevel):
    def __init__(self,parent):
        super().__init__(parent)
        self.geometry("200x500")
        self.title("Vendas")