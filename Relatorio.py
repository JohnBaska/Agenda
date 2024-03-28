from tkinter import *
from Funcoes import *

from reportlab.pdfgen import canvas
import webbrowser


class Relatorio (Funcoes):
    def print_cadastro (self):
        webbrowser.open("cadastro.pdf")
    
    def gera_relatorio (self):
        self.variaveis()
        self.c = canvas.Canvas ("cliente.pdf")

        self.c.setFont("Helvetica-Bold", 24)
        self.c.drawString(200, 790, 'Ficha do cadastrado')

        self.c.setFont("Helvetica-Bold", 18)
        self.c.drawString(35, 700, 'Nome: ')
        self.c.drawString(375, 700, 'Codigo: ')
        self.c.drawString(35, 670, 'E-mail: ')
        self.c.drawString(375, 670, 'Telefone: ')
        self.c.drawString(35, 640, 'Estado: ')
        self.c.drawString(260, 640, 'Cidade: ')
        self.c.drawString(35, 610, 'Bairro: ')
        self.c.drawString(260, 610, 'Complemento: ')

        self.c.setFont("Helvetica", 18)
        self.c.drawString(95, 700, self.Nome)
        self.c.drawString(455, 700, self.Cod)
        self.c.drawString(100, 670, self.E_mail)
        self.c.drawString(460, 670, self.Telefone)
        self.c.drawString(105, 640, self.Estado)
        self.c.drawString(330, 640, self.Cidade)
        self.c.drawString(105, 610, self.Bairro)
        self.c.drawString(390, 610, self.Complemento)

        self.c.rect(20, 590, 575, 130, fill= False, stroke= True)

        self.c.showPage()
        self.c.save()
        self.print_cadastro()
