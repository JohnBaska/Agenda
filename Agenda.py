from tkinter import *
from tkinter import ttk
from Relatorio import *
from Informacoes import *

class Agenda(Relatorio, Informacoes):
    #Função principal
    def __init__ (self):
        self.janela = Tk()
        self.tela()
        self.frame_de_tela()
        self.informacoes()
        self.buttons()
        self.treeview()
        self.monta_tabela()
        self.select_lista()
        self.Menus()
        self.janela.mainloop()
    #Funcao para mudar a configuracoes da janela
    def tela(self):
        ###Titulo da janela
        self.janela.title("Agenda de Contatos")

        ###Cor de fundo da janela
        self.janela.configure(background= "Navy")
        
        ###Tamanho original da janela
        self.janela.geometry("950x600")
        
        ###Permissão para mudar a janela de tamanho
        self.janela.resizable(TRUE, TRUE)
        
        ###Tamanho maximo que a janela pode alcancar
        self.janela.maxsize(width=1900, height=1200)
        
        ###Tamanho minimo que a janela pode alcancar
        self.janela.minsize(width=475, height=300)
    #Criacao dos frames de tela
    def frame_de_tela(self):
        ###Frame: um poligoono regular de 4 lados que fica dentro da janela como uma subjanela
        ###bg:cor de fundo do frame
        ###highlightbackground: cor da borda
        ###highlightthickness: largura da borda
        self.frame_1 = Frame(self.janela, bg="lightblue", highlightbackground="darkslateblue", highlightthickness= 4)
        self.canvas_bt = Canvas(self.frame_1, bd= 0, bg= 'black', highlightbackground= 'gray', highlightthickness= 3)
        self.canvas_bt_2 = Canvas(self.frame_1, bd= 0, bg= 'black', highlightbackground= 'gray', highlightthickness= 3)
        self.frame_2 = Frame(self.janela, bg="lightblue", highlightbackground="darkslateblue", highlightthickness=3)

        
        ###relx: Em qual porcentagem da tela se inicia da esqauerda para a direita
        ###rely: Em qual porcentagem da tela se inicia de cima para baixo
        ###relwidth: Qual porcentagem da tela, da esquerda para direita ele vai ocupar
        ###relwidth: Qual porcentagem da tela, de cima para baixo ele vai ocupar
        self.frame_1.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.48)
        self.canvas_bt.place(relx=0.046, rely= 0.84, relwidth= 0.2075, relheight=0.12)
        self.canvas_bt_2.place(relx=0.626, rely= 0.84, relwidth= 0.3075, relheight=0.12)
        self.frame_2.place(relx=0.01, rely=0.50, relwidth=0.98, relheight=0.48)
    #Coleta de dados
    def Cidades (self):
        Label(self.Cadastro, text="Cidade: ", bg="DodgerBlue", fg="indigo").place(relx=0.18, rely=0.53)
        self.cidade = StringVar(self.Cadastro)
        self.cidade.set("CIDADE")
        self.Cidade_entry = OptionMenu(self.Cadastro, self.cidade, "                                                ")
        self.Cidade_entry.place(relx=0.18, rely=0.61, relwidth=0.25, relheight=0.08)

        if self.estado == "Minas Gerais":
            self.Cidades_MG()
            self.Cidade_entry = OptionMenu(self.Cadastro, self.cidade, *self.cidades)
            self.Cidade_entry.place(relx=0.18, rely=0.61, relwidth=0.25, relheight=0.08)

        Label(self.Cadastro, text="Cidade: ", bg="DodgerBlue", fg="indigo").place(relx=0.18, rely=0.53)
        self.cidade1 = StringVar(self.Cadastro)
        self.cidade1.set("CIDADE")
        self.Cidade1_entry = OptionMenu(self.Cadastro, self.cidade1, "                                           ")
        self.Cidade1_entry.place(relx=0.18, rely=0.61, relwidth=0.25, relheight=0.08)

        if self.estado1 == "Minas Gerais":
            self.Cidades_MG()
            self.Cidade1_entry = OptionMenu(self.Alteração, self.cidade1, *self.cidades)
            self.Cidade1_entry.place(relx=0.18, rely=0.61, relwidth=0.25, relheight=0.08)
        
        Label(self.Cadastro, text="Cidade: ", bg="DodgerBlue", fg="indigo").place(relx=0.18, rely=0.53)
        self.cidade2 = StringVar(self.Cadastro)
        self.cidade2.set("CIDADE")
        self.Cidade2_entry = OptionMenu(self.Cadastro, self.cidade2, "                                            ")
        self.Cidade2_entry.place(relx=0.18, rely=0.61, relwidth=0.25, relheight=0.08)

        if self.estado2 == "Minas Gerais":
            self.Cidades_MG()
            self.Cidade2_entry = OptionMenu(self.Busca, self.cidade2, *self.cidades)
            self.Cidade2_entry.place(relx=0.18, rely=0.61, relwidth=0.25, relheight=0.08)

        Label(self.Exclusão, text="Cidade: ", bg="DodgerBlue", fg="indigo").place(relx=0.18, rely=0.53)
        self.cidade3 = StringVar(self.Exclusão)
        self.cidade3.set("CIDADE")
        self.Cidade3_entry = OptionMenu(self.Exclusão, self.cidade3, "                                             ")
        self.Cidade3_entry.place(relx=0.18, rely=0.61, relwidth=0.25, relheight=0.08)
        
        if self.estado3 == "Minas Gerais":
            self.Cidades_MG()
            self.Cidade3_entry = OptionMenu(self.Exclusão, self.cidade3, *self.cidades)
            self.Cidade3_entry.place(relx=0.18, rely=0.61, relwidth=0.25, relheight=0.08)

    def informacoes (self):
        ###Criação das abas
        self.abas = ttk.Notebook(self.frame_1)
        self.Cadastro = Frame(self.abas)
        self.Alteração = Frame(self.abas)
        self.Busca = Frame(self.abas)
        self.Exclusão = Frame(self.abas)

        #mudando a cor de fundo delas...
        self.Cadastro.configure(background= "DodgerBlue")
        self.Alteração.configure(background= "DodgerBlue")
        self.Busca.configure(background= "DodgerBlue")
        self.Exclusão.configure(background= "DodgerBlue")
        
        #colocando um título em cada uma...
        self.abas.add(self.Cadastro, text= "Cadastrar")
        self.abas.add(self.Alteração, text= "Alterar")
        self.abas.add(self.Busca, text= "Buscar")
        self.abas.add(self.Exclusão, text= "Excluir")
        
        #posionando cada uma em frame de cima.
        self.abas.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.98)
        
        ###Lugares onde ficaram as informações

        #nome
        Label(self.Cadastro, text="Nome: ", bg="DodgerBlue", fg="indigo").place(relx=0.05, rely=0.01)
        self.Nome_entry = Entry(self.Cadastro, bg='#dfe3ee', fg='#107bd2', font=("Verdana", 13))
        self.Nome_entry.place(relx=0.05, rely=0.09, relwidth=0.6, relheight=0.08)

        Label(self.Alteração, text="Nome: ", bg="DodgerBlue", fg="indigo").place(relx=0.05, rely=0.01)
        self.Nome1_entry = Entry(self.Alteração, bg='#dfe3ee', fg='#107bd2', font=("Verdana", 13))
        self.Nome1_entry.place(relx=0.05, rely=0.09, relwidth=0.6, relheight=0.08)

        Label(self.Busca, text="Nome: ", bg="DodgerBlue", fg="indigo").place(relx=0.05, rely=0.01)
        self.Nome2_entry = Entry(self.Busca, bg='#dfe3ee', fg='#107bd2', font=("Verdana", 13))
        self.Nome2_entry.place(relx=0.05, rely=0.09, relwidth=0.6, relheight=0.08)

        Label(self.Exclusão, text="Nome: ", bg="DodgerBlue", fg="indigo").place(relx=0.05, rely=0.01)
        self.Nome3_entry = Entry(self.Exclusão, bg='#dfe3ee', fg='#107bd2', font=("Verdana", 13))
        self.Nome3_entry.place(relx=0.05, rely=0.09, relwidth=0.6, relheight=0.08)

        #código
        Label(self.Cadastro, text="Codigo: ", bg="DodgerBlue", fg="indigo").place(relx=0.75, rely=0.01)
        self.Cod_entry = Entry(self.Cadastro, bg='#dfe3ee', fg='#107bd2', font=("Verdana", 13))
        self.Cod_entry.place(relx=0.75, rely=0.09, relwidth=0.2, relheight=0.08)

        Label(self.Alteração, text="Codigo: ", bg="DodgerBlue", fg="indigo").place(relx=0.75, rely=0.01)
        self.Cod1_entry = Entry(self.Alteração, bg='#dfe3ee', fg='#107bd2', font=("Verdana", 13))
        self.Cod1_entry.place(relx=0.75, rely=0.09, relwidth=0.2, relheight=0.08)

        Label(self.Busca, text="Codigo: ", bg="DodgerBlue", fg="indigo").place(relx=0.75, rely=0.01)
        self.Cod2_entry = Entry(self.Busca, bg='#dfe3ee', fg='#107bd2', font=("Verdana", 13))
        self.Cod2_entry.place(relx=0.75, rely=0.09, relwidth=0.2, relheight=0.08)

        Label(self.Exclusão, text="Codigo: ", bg="DodgerBlue", fg="indigo").place(relx=0.75, rely=0.01)
        self.Cod3_entry = Entry(self.Exclusão, bg='#dfe3ee', fg='#107bd2', font=("Verdana", 13))
        self.Cod3_entry.place(relx=0.75, rely=0.09, relwidth=0.2, relheight=0.08)

        #e-mail 
        Label(self.Cadastro, text="E-mail: ", bg="DodgerBlue", fg="indigo").place(relx=0.05, rely=0.255)
        self.E_mail_entry = Entry(self.Cadastro, bg='#dfe3ee', fg='#107bd2', font=("Verdana", 13))
        self.E_mail_entry.place(relx=0.05, rely=0.335, relwidth=0.5, relheight=0.08)
        
        Label(self.Alteração, text="E-mail: ", bg="DodgerBlue", fg="indigo").place(relx=0.05, rely=0.255)
        self.E_mail1_entry = Entry(self.Alteração, bg='#dfe3ee', fg='#107bd2', font=("Verdana", 13))
        self.E_mail1_entry.place(relx=0.05, rely=0.335, relwidth=0.5, relheight=0.08)

        Label(self.Busca, text="E-mail: ", bg="DodgerBlue", fg="indigo").place(relx=0.05, rely=0.255)
        self.E_mail2_entry = Entry(self.Busca, bg='#dfe3ee', fg='#107bd2', font=("Verdana", 13))
        self.E_mail2_entry.place(relx=0.05, rely=0.335, relwidth=0.5, relheight=0.08)

        Label(self.Exclusão, text="E-mail: ", bg="DodgerBlue", fg="indigo").place(relx=0.05, rely=0.255)
        self.E_mail3_entry = Entry(self.Exclusão, bg='#dfe3ee', fg='#107bd2', font=("Verdana", 13))
        self.E_mail3_entry.place(relx=0.05, rely=0.335, relwidth=0.5, relheight=0.08)

        #telefone
        Label(self.Cadastro, text="Telefone: ", bg="DodgerBlue", fg="indigo").place(relx=0.7, rely=0.255)
        self.Telefone_entry = Entry(self.Cadastro, bg='#dfe3ee', fg='#107bd2', font=("Verdana", 13))
        self.Telefone_entry.place(relx=0.7, rely=0.335, relwidth=0.25, relheight=0.08)

        Label(self.Alteração, text="Telefone: ", bg="DodgerBlue", fg="indigo").place(relx=0.7, rely=0.255)
        self.Telefone1_entry = Entry(self.Alteração, bg='#dfe3ee', fg='#107bd2', font=("Verdana", 13))
        self.Telefone1_entry.place(relx=0.7, rely=0.335, relwidth=0.25, relheight=0.08)

        Label(self.Busca, text="Telefone: ", bg="DodgerBlue", fg="indigo").place(relx=0.7, rely=0.255)
        self.Telefone2_entry = Entry(self.Busca, bg='#dfe3ee', fg='#107bd2', font=("Verdana", 13))
        self.Telefone2_entry.place(relx=0.7, rely=0.335, relwidth=0.25, relheight=0.08)

        Label(self.Exclusão, text="Telefone: ", bg="DodgerBlue", fg="indigo").place(relx=0.7, rely=0.255)
        self.Telefone3_entry = Entry(self.Exclusão, bg='#dfe3ee', fg='#107bd2', font=("Verdana", 13))
        self.Telefone3_entry.place(relx=0.7, rely=0.335, relwidth=0.25, relheight=0.08)
        
        #estado
        self.Estados()

        Label(self.Cadastro, text="Estado: ", bg="DodgerBlue", fg="indigo").place(relx=0.05, rely=0.53)
        self.estado = StringVar(self.Cadastro)
        self.estado.set("ESTADO")
        self.Estado_entry = OptionMenu(self.Cadastro, self.estado, *self.estados)
        self.Estado_entry.place(relx=0.05, rely=0.61, relwidth=0.1, relheight=0.08)

        Label(self.Alteração, text="Estado: ", bg="DodgerBlue", fg="indigo").place(relx=0.05, rely=0.53)
        self.estado1 = StringVar(self.Alteração)
        self.estado1.set("ESTADO")
        self.Estado_entry = OptionMenu(self.Alteração, self.estado, *self.estados)
        self.Estado_entry.place(relx=0.05, rely=0.61, relwidth=0.1, relheight=0.08)

        Label(self.Busca, text="Estado: ", bg="DodgerBlue", fg="indigo").place(relx=0.05, rely=0.53)
        self.estado2 = StringVar(self.Busca)
        self.estado2.set("ESTADO")
        self.Estado_entry = OptionMenu(self.Busca, self.estado, *self.estados)
        self.Estado_entry.place(relx=0.05, rely=0.61, relwidth=0.1, relheight=0.08)

        Label(self.Exclusão, text="Estado: ", bg="DodgerBlue", fg="indigo").place(relx=0.05, rely=0.53)
        self.estado3 = StringVar(self.Exclusão)
        self.estado3.set("ESTADO")
        self.Estado_entry = OptionMenu(self.Exclusão, self.estado, *self.estados)
        self.Estado_entry.place(relx=0.05, rely=0.61, relwidth=0.1, relheight=0.08)

        #cidade
        self.Cidades()

        #bairro
        Label(self.Cadastro, text="Bairro: ", bg="DodgerBlue", fg="indigo").place(relx=0.46, rely=0.53)
        self.Bairro_entry = Entry(self.Cadastro, bg='#dfe3ee', fg='#107bd2', font=("Verdana", 13))
        self.Bairro_entry.place(relx=0.46, rely=0.61, relwidth=0.21, relheight=0.08)

        Label(self.Alteração, text="Bairro: ", bg="DodgerBlue", fg="indigo").place(relx=0.46, rely=0.53)
        self.Bairro1_entry = Entry(self.Alteração, bg='#dfe3ee', fg='#107bd2', font=("Verdana", 13))
        self.Bairro1_entry.place(relx=0.46, rely=0.61, relwidth=0.21, relheight=0.08)

        Label(self.Busca, text="Bairro: ", bg="DodgerBlue", fg="indigo").place(relx=0.46, rely=0.53)
        self.Bairro2_entry = Entry(self.Busca, bg='#dfe3ee', fg='#107bd2', font=("Verdana", 13))
        self.Bairro2_entry.place(relx=0.46, rely=0.61, relwidth=0.21, relheight=0.08)

        Label(self.Exclusão, text="Bairro: ", bg="DodgerBlue", fg="indigo").place(relx=0.46, rely=0.53)
        self.Bairro3_entry = Entry(self.Exclusão, bg='#dfe3ee', fg='#107bd2', font=("Verdana", 13))
        self.Bairro3_entry.place(relx=0.46, rely=0.61, relwidth=0.21, relheight=0.08)

        #complemento
        Label(self.Cadastro, text="Complemento: ", bg="DodgerBlue", fg="indigo").place(relx=0.70, rely=0.53)
        self.Complemento_entry = Entry(self.Cadastro, bg='#dfe3ee', fg='#107bd2', font=("Verdana", 13))
        self.Complemento_entry.place(relx=0.70, rely=0.61, relwidth=0.25, relheight=0.08)

        Label(self.Alteração, text="Complemento: ", bg="DodgerBlue", fg="indigo").place(relx=0.70, rely=0.53)
        self.Complemento1_entry = Entry(self.Alteração, bg='#dfe3ee', fg='#107bd2', font=("Verdana", 13))
        self.Complemento1_entry.place(relx=0.70, rely=0.61, relwidth=0.25, relheight=0.08)

        Label(self.Busca, text="Complemento: ", bg="DodgerBlue", fg="indigo").place(relx=0.70, rely=0.53)
        self.Complemento2_entry = Entry(self.Busca, bg='#dfe3ee', fg='#107bd2', font=("Verdana", 13))
        self.Complemento2_entry.place(relx=0.70, rely=0.61, relwidth=0.25, relheight=0.08)

        Label(self.Exclusão, text="Complemento: ", bg="DodgerBlue", fg="indigo").place(relx=0.70, rely=0.53)
        self.Complemento3_entry = Entry(self.Exclusão, bg='#dfe3ee', fg='#107bd2', font=("Verdana", 13))
        self.Complemento3_entry.place(relx=0.70, rely=0.61, relwidth=0.25, relheight=0.08)
    #Criacao dos botoes
    def buttons (self):
        ###Botao Cadastrar
        self.cadastrar = Button(self.Cadastro, text="Casdastrar", command= self.novo_cadastro, fg="white", bd=1, bg="mediumblue", highlightbackground="royalblue", highlightthickness=5, font=('verdanda', 10, 'bold'))
        self.cadastrar.place(relx=0.05, rely=0.85, relwidth=0.10, relheight=0.1)
        self.cadastrar.bind("<Enter>", func=lambda e: self.cadastrar.config(background="steelblue"))
        self.cadastrar.bind("<Leave>", func=lambda e: self.cadastrar.config(background="mediumblue"))

        ###Botao Alterar
        self.Alterar = Button(self.Alteração, text="Alterar", command=self.altera_cadastro, fg="white", bd=1, bg="mediumblue", highlightbackground="royalblue", highlightthickness=5, font=('verdanda', 10, 'bold'))
        self.Alterar.place(relx=0.05, rely=0.85, relwidth=0.10, relheight=0.1)
        self.Alterar.bind("<Enter>", func=lambda e: self.Alterar.config(background="steelblue"))
        self.Alterar.bind("<Leave>", func=lambda e: self.Alterar.config(background="mediumblue"))

        ###Botao Buscar
        self.Buscar = Button(self.Busca, text="Buscar", command=self.busca_cadastro, fg="white", bd=1, bg="mediumblue", highlightbackground="royalblue", highlightthickness=5, font=('verdanda', 10, 'bold'))
        self.Buscar.place(relx=0.05, rely=0.85, relwidth=0.10, relheight=0.1)
        self.Buscar.bind("<Enter>", func=lambda e: self.Buscar.config(background="steelblue"))
        self.Buscar.bind("<Leave>", func=lambda e: self.Buscar.config(background="mediumblue"))

        ###Botao Excluir
        self.Excluir = Button(self.Exclusão, text="Excluir",  command=self.exclui_cadastro, fg="white", bd=1, bg="mediumblue", highlightbackground="royalblue", highlightthickness=5, font=('verdanda', 10, 'bold'))
        self.Excluir.place(relx=0.05, rely=0.85, relwidth=0.10, relheight=0.1)
        self.Excluir.bind("<Enter>", func=lambda e: self.Excluir.config(background="steelblue"))
        self.Excluir.bind("<Leave>", func=lambda e: self.Excluir.config(background="mediumblue"))

        ###Botao Limpar
        self.Apagar = Button(self.Cadastro, text="Limpar", command=self.limpa_tela, fg="white", bd=1, bg="mediumblue", highlightbackground="royalblue", highlightthickness=5, font=('verdanda', 10, 'bold'))
        self.Apagar.place(relx=0.83, rely=0.85, relwidth=0.10, relheight=0.1)
        self.Apagar.bind("<Enter>", func=lambda e: self.Apagar.config(background="steelblue"))
        self.Apagar.bind("<Leave>", func=lambda e: self.Apagar.config(background="mediumblue"))

        self.Apagar = Button(self.Alteração, text="Limpar", command=self.limpa1_tela, fg="white", bd=1, bg="mediumblue", highlightbackground="royalblue", highlightthickness=5, font=('verdanda', 10, 'bold'))
        self.Apagar.place(relx=0.83, rely=0.85, relwidth=0.10, relheight=0.1)
        self.Apagar.bind("<Enter>", func=lambda e: self.Apagar.config(background="steelblue"))
        self.Apagar.bind("<Leave>", func=lambda e: self.Apagar.config(background="mediumblue"))

        self.Apagar = Button(self.Busca, text="Limpar", command=self.limpa2_tela, fg="white", bd=1, bg="mediumblue", highlightbackground="royalblue", highlightthickness=5, font=('verdanda', 10, 'bold'))
        self.Apagar.place(relx=0.83, rely=0.85, relwidth=0.10, relheight=0.1)
        self.Apagar.bind("<Enter>", func=lambda e: self.Apagar.config(background="steelblue"))
        self.Apagar.bind("<Leave>", func=lambda e: self.Apagar.config(background="mediumblue"))

        self.Apagar = Button(self.Exclusão, text="Limpar", command=self.limpa3_tela, fg="white", bd=1, bg="mediumblue", highlightbackground="royalblue", highlightthickness=5, font=('verdanda', 10, 'bold'))
        self.Apagar.place(relx=0.83, rely=0.85, relwidth=0.10, relheight=0.1)
        self.Apagar.bind("<Enter>", func=lambda e: self.Apagar.config(background="steelblue"))
        self.Apagar.bind("<Leave>", func=lambda e: self.Apagar.config(background="mediumblue"))
    #Criacao de uma treview frame 2
    def treeview (self):
        ###Criando a treview...
        self.tabela_cadastrados = ttk.Treeview(self.frame_2, height=3, column=("col1", "col2", "col3"), style="")
        
        #titulando as colunas...
        self.tabela_cadastrados.heading("#0", text="")
        self.tabela_cadastrados.heading("#1", text="Codigo")
        self.tabela_cadastrados.heading("#2", text="Nome")
        self.tabela_cadastrados.heading("#3", text="Telefone")

        #espaçando cada uma delas...
        self.tabela_cadastrados.column("#0", width=1)
        self.tabela_cadastrados.column("col1", width=100)
        self.tabela_cadastrados.column("col2", width=400)
        self.tabela_cadastrados.column("col3", width=100)
        
        #posionando a treview.
        self.tabela_cadastrados.place(relx=0.01, rely=0.075, relwidth=0.95, relheight=0.85)
        
        ###Criando uma barra de rolamento
        self.scroll_tabela = Scrollbar(self.frame_2, orient='vertical')
        self.tabela_cadastrados.configure(yscroll=self.scroll_tabela.set)
        self.scroll_tabela.place(relx=0.96, rely=0.075, relwidth=0.03, relheight=0.85)

        ###Cofigurando o duplo click
        self.tabela_cadastrados.bind("<Double-1>", self.duplo_click)
    #Criando Menus
    def Menus(self):
        ###Criando dois menus...
        menubar = Menu(self.janela)
        self.janela.config(menu=menubar)
        filemenu = Menu(menubar)
        filemenu2 = Menu(menubar)
        
        #criando uma função para sair da Agenda...
        def Quit(): self.janela.destroy()
        
        #tiitulando cada um dos menus
        menubar.add_cascade(label= "Opções", menu= filemenu)
        menubar.add_cascade(label= "Relatorios", menu= filemenu2)
        
        #acrecentando funções no menu opções
        filemenu.add_command(label="Sair", command=Quit)
        filemenu.add_command(label="Limpar", command=self.limpa_telas)
        
        #acrescentando funções no menu8 relatório
        filemenu2.add_command(label="Ficha de Cadastro", command=self.gera_relatorio)