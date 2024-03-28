#IMPORTANTE

"""No momento estou fazendo a mudança da entrada de cidade para um option menu, porém tenho que pesquisar como fazer para mudar a 
opções do menu sempre que o usuario clicar nele"""

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3
from Agenda import *

class Login (Agenda):
    #Função principal
    def __init__(self):
        self.log = Tk()
        self.tela_login()
        self.frame_de_tela_login()
        self.monta_tabela_login()
        self.informações()
        self.botões_login()
        self.log.mainloop()
    #Configurações da tela de login
    def tela_login (self):
        ###Titulo da janela
        self.log.title("Login")

        ###Cor de fundo da janela
        self.log.configure(background= "Navy")
        
        ###Tamanho original da janela
        self.log.geometry("300x400")
        
        ###Permissão para mudar a janela de tamanho
        self.log.resizable(TRUE, TRUE)
        
        ###Tamanho maximo que a janela pode alcancar
        self.log.maxsize(width=450, height=600)
        
        ###Tamanho minimo que a janela pode alcancar
        self.log.minsize(width=150, height=200)
    #inserindo um frame na tela
    def frame_de_tela_login (self):
        ###Criando o frame
        self.frame = Frame(self.log, bg="lightblue", highlightbackground="darkslateblue", highlightthickness= 4)
        
        ###localizando o frame na tela de login
        self.frame.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.98)
    #Função para limpar os campos da tela de login
    def limpa_tela_login (self):
        self.Senha_cadastro.delete(0, END)
        self.Nome_cadastro.delete(0, END)
        self.Senha_login.delete(0, END)
        self.Nome_login.delete(0, END)
    #Conecta o banco de dados onde se encontra os logins 
    def conecta_bd_login(self):
        self.conn = sqlite3.connect("login.bd")
        self.cursor = self.conn.cursor(); print('Conectando ao banco de dados')
    #Desconecta o banco de dados 
    def desconecta_bd_login(self):
        #Fecha o banco de dados
        self.conn.close(); print("Banco de dados desconectado")
    #Cria o banco de dados
    def monta_tabela_login(self):
        self.conecta_bd_login()
        ###Criar tabela dentro do banco de dados
        self.cursor.execute("""
                        CREATE TABLE IF NOT EXISTS login (
                            Nome CHAR(50) PRIMARY KEY,
                            Senha CHAR(30) NOT NULL
                        );
                    """)
        #Salva as alterações
        self.conn.commit(); print("Banco de dados criado")
        self.desconecta_bd_login()
    #Salva novo cadastro dentro do banco de dados
    def novo_cadastro_login (self):
        self.conecta_bd_login()
        Nome = self.Nome_cadastro.get()
        msg = ""

        ###Verifica se o nome cadastrados contém algum caracter indevido.
        for i in range(len(Nome)):
            if Nome[i] == " " and msg == "":
                msg = "O Nome não pode ter espaco (' ')"
        ###Se achar algum caractr indevido...
        if msg != "":
            #imprima a mensagem.
            messagebox.showinfo("Aviso!!!", msg) 
        #Se não encontrar e todos os campos estiverem preenchidos...
        elif self.Senha_cadastro.get() != "" and self.Nome_cadastro.get() != "":
            #inserir no banco de dados o novo cadastro...
            self.cursor.execute("""INSERT INTO login (Nome, Senha)
                                    VALUES (?, ?)""", (self.Nome_cadastro.get(), self.Senha_cadastro.get()))
            ##Salvar as alterações feitas no banco.
            self.conn.commit()
            self.desconecta_bd_login()
            self.limpa_tela_login()
        #Se não encontrar e algum não estiver preenchido...
        else: 
            #Aviso ao usuario.
            msg = "Para realização do cadastro é obrigatório o preenchimento \ndas áreas 'Nome' e 'Senha'"
            messagebox.showinfo("Aviso!!!", msg)    
    #Informações dentro da janela login
    def informações (self):
    ###Criando as abas login e cadastro...
        self.abas_login = ttk.Notebook(self.frame)
        self.login = Frame(self.abas_login)
        self.cadastro = Frame(self.abas_login)
        
        #configurando a cor de fundo...
        self.login.configure(background= "lightBlue")
        self.cadastro.configure(background= "lightBlue")
        
        #configurando o título da aba...
        self.abas_login.add(self.login, text= "Logar")
        self.abas_login.add(self.cadastro, text= "Cadastrar")
        
        #poosionamento das abas dentro do frame.
        self.abas_login.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.98)
        
    ###Informações dentro da aba login...

        #titulo da aba...
        Label(self.login, text="Login", bg="lightBlue", fg="indigo", font=("Verdana", 20)).place(relx=0.35, rely=0.02)

        #nome passado pelo usuario...
        Label(self.login, text="Nome: ", bg="lightBlue", fg="indigo").place(relx=0.05, rely=0.2)
        self.Nome_login = Entry(self.login, bg='#dfe3ee', fg='#107bd2', font=("Verdana", 13))
        self.Nome_login.place(relx=0.05, rely=0.28, relwidth=0.9, relheight=0.08)
        
        #senha passada pelo usuario.
        Label(self.login, text="Senha: ", bg="lightBlue", fg="indigo").place(relx=0.05, rely=0.45)
        self.Senha_login = Entry(self.login, bg='#dfe3ee', fg='#107bd2', font=("Verdana", 13), show='*')
        self.Senha_login.place(relx=0.05, rely=0.53, relwidth=0.9, relheight=0.08)
        
    ###Informções dentro da aba cadastro

        #título da aba...
        Label(self.cadastro, text="Cadastro", bg="lightBlue", fg="indigo", font=("Verdana", 20)).place(relx=0.30, rely=0.02)

        #nome passado pelo usuario...
        Label(self.cadastro, text="Nome: ", bg="lightBlue", fg="indigo").place(relx=0.05, rely=0.2)
        self.Nome_cadastro = Entry(self.cadastro, bg='#dfe3ee', fg='#107bd2', font=("Verdana", 13))
        self.Nome_cadastro.place(relx=0.05, rely=0.28, relwidth=0.9, relheight=0.08)
        
        #senha passado pelo usuario.
        Label(self.cadastro, text="Senha: ", bg="lightBlue", fg="indigo").place(relx=0.05, rely=0.45)
        self.Senha_cadastro = Entry(self.cadastro, bg='#dfe3ee', fg='#107bd2', font=("Verdana", 13), show= '*')
        self.Senha_cadastro.place(relx=0.05, rely=0.53, relwidth=0.9, relheight=0.08)
    #Função que procura dentro do banco de dados o cadastro do usuario
    def procura_no_banco(self):
        self.conecta_bd_login()
        lista = self.cursor.execute(""" SELECT Nome, Senha FROM login""")

        nome = ""
        senha = ""
        entrou = FALSE
        
        ###Procurando o cadastro...
 
        #passa por todas os cadastro um por um...
        for i in lista:
            #enquanto não estiver encontrado...
            if entrou == FALSE:
                #Pegar as duas informações do cadstro e...
                for c in range(len(i)):
                    #se for a primeira...
                    if c == 0:
                        #guarda dentro do nome...
                        nome = i[c]
                    #se for a segunda...
                    else:
                        #guarda dentro da senha.
                        senha = i[c]

                #Verifica se o cadastro foi encontrado...            
                if self.Nome_login.get() == nome and self.Senha_login.get() == senha:
                    #se sim...
                    self.desconecta_bd_login()
                    #destroi a janela de login...
                    self.log.destroy()
                    #avisa ao usuario...
                    msg = "Login feito com Sucesso"
                    messagebox.showinfo("Aviso!!!", msg)
                    #guarda o nome do usuario...
                    self.usuario = nome
                    #acesssa a agenda...
                    Agenda.__init__(self)
                    #informar ao programa que o login foi encontrado
                    entrou = TRUE
        
        #Se o login não for encotrado...
        if entrou == FALSE:
            self.desconecta_bd_login()
            #avisa ao usuario...
            msg = "Cadastro não existente"
            messagebox.showinfo("Aviso!!!", msg)
            #limpa a tela.
            self.limpa_tela_login()
    #Botões de logar e cadastrar
    def botões_login (self):
        ###Botao logar
        self.logar = Button(self.login, text="Logar", command= self.procura_no_banco, fg="white", bd=1, bg="mediumblue", highlightbackground="royalblue", highlightthickness=5, font=('verdanda', 10, 'bold'))
        self.logar.place(relx=0.15, rely=0.70, relwidth=0.70, relheight=0.1)
        self.logar.bind("<Enter>", func=lambda e: self.logar.config(background="steelblue"))
        self.logar.bind("<Leave>", func=lambda e: self.logar.config(background="mediumblue"))
        
        ###Botão cadastrar
        self.cadastrar_login = Button(self.cadastro, text="Cadastrar", command= self.novo_cadastro_login, fg="white", bd=1, bg="mediumblue", highlightbackground="royalblue", highlightthickness=5, font=('verdanda', 10, 'bold'))
        self.cadastrar_login.place(relx=0.15, rely=0.70, relwidth=0.70, relheight=0.1)
        self.cadastrar_login.bind("<Enter>", func=lambda e: self.cadastrar_login.config(background="steelblue"))
        self.cadastrar_login.bind("<Leave>", func=lambda e: self.cadastrar_login.config(background="mediumblue"))
        
Login()