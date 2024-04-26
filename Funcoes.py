from tkinter import *
from tkinter import messagebox
import sqlite3

class Funcoes():
    def limpa_telas (self):
        #Esvazia os campos de cadastro
        self.Nome_entry.delete(0, END)
        self.Cod_entry.delete(0, END)
        self.Telefone_entry.delete(0, END)
        self.estado.set("ESTADO")
        self.cidade.set("CIDADE")
        self.Bairro_entry.delete(0, END)
        self.Complemento_entry.delete(0, END)
        self.E_mail_entry.delete(0, END)

        Label(self.Cadastro, text="Código já cadastrado", bg="dodgerblue", fg="dodgerblue").place(relx=0.25, rely=0.01)
        Label(self.Cadastro, text="Para realização do cadastro é obrigatório o preenchimento das áreas 'Nome' e 'Codigo'", bg="dodgerblue", fg="dodgerblue").place(relx=0.25, rely=0.01)

        #Esvazia os campos de cadastro
        self.Nome1_entry.delete(0, END)
        self.Cod1_entry.delete(0, END)
        self.Telefone1_entry.delete(0, END)
        self.estado1.set("ESTADO")
        self.cidade1.set("CIDADE")
        self.Bairro1_entry.delete(0, END)
        self.Complemento1_entry.delete(0, END)
        self.E_mail1_entry.delete(0, END)

        #Esvazia os campos de cadastro
        self.Nome2_entry.delete(0, END)
        self.Cod2_entry.delete(0, END)
        self.Telefone2_entry.delete(0, END)
        self.E_mail2_entry.delete(0, END)

        #Esvazia os campos de cadastro
        self.Nome3_entry.delete(0, END)
        self.Cod3_entry.delete(0, END)
        self.Telefone3_entry.delete(0, END)
        self.E_mail3_entry.delete(0, END)

        Label(self.Exclusão, text="Coloque o codigo do cadastro para exclui-lo", bg="dodgerblue", fg="dodgerblue").place(relx=0.35, rely=0.01)

    #Limpa todos os campos do cadastro
    def limpa_tela (self):
        #Esvazia os campos de cadastro
        self.Nome_entry.delete(0, END)
        self.Cod_entry.delete(0, END)
        self.Telefone_entry.delete(0, END)
        self.estado.set("ESTADO")
        self.cidade.set("CIDADE")
        self.Bairro_entry.delete(0, END)
        self.Complemento_entry.delete(0, END)
        self.E_mail_entry.delete(0, END)

        Label(self.Cadastro, text="Código já cadastrado", bg="dodgerblue", fg="dodgerblue").place(relx=0.25, rely=0.01)
        Label(self.Cadastro, text="Para realização do cadastro é obrigatório o preenchimento das áreas 'Nome' e 'Codigo'", bg="dodgerblue", fg="dodgerblue").place(relx=0.25, rely=0.01)
    def limpa1_tela (self):
        #Esvazia os campos de cadastro
        self.Nome1_entry.delete(0, END)
        self.Cod1_entry.delete(0, END)
        self.Telefone1_entry.delete(0, END)
        self.estado1.set("ESTADO")
        self.cidade1.set("CIDADE")
        self.Bairro1_entry.delete(0, END)
        self.Complemento1_entry.delete(0, END)
        self.E_mail1_entry.delete(0, END)
    def limpa2_tela (self):
        #Esvazia os campos de cadastro
        self.Nome2_entry.delete(0, END)
        self.Cod2_entry.delete(0, END)
        self.Telefone2_entry.delete(0, END)
        self.E_mail2_entry.delete(0, END)
    def limpa3_tela (self):
        #Esvazia os campos de cadastro
        self.Nome3_entry.delete(0, END)
        self.Cod3_entry.delete(0, END)
        self.Telefone3_entry.delete(0, END)
        self.E_mail3_entry.delete(0, END)

        Label(self.Exclusão, text="Coloque o codigo do cadastro para exclui-lo", bg="dodgerblue", fg="dodgerblue").place(relx=0.35, rely=0.01)
    #Conecta o banco de dados
    def conecta_bd(self):
        #conecta ao banco de dados "cadastros.bd"
        self.conn = sqlite3.connect(f"{self.usuario}.bd")
        self.cursor = self.conn.cursor(); print('Conectando ao banco de dados')
    #Desconecta o banco de dados 
    def desconecta_bd(self):
        #Fecha o banco de dados
        self.conn.close(); print("Banco de dados desconectado")
    #Monta o banco de dados
    def monta_tabela(self):
        self.conecta_bd()
        ###Criar tabela dentro do banco de dados
        self.cursor.execute(f"""
                        CREATE TABLE IF NOT EXISTS {self.usuario} (
                            Cod CHAR(10) PRIMARY KEY,
                            Nome CHAR(50) NOT NULL,
                            Telefone CHAR (30),
                            Estado CHAR(2),
                            Cidade CHAR(80),
                            Bairro CHAR(80),
                            Complemento CHAR(80),
                            Email CHAR(50)
                        );
                    """)
        #Salva as alterações
        self.conn.commit(); print("Banco de dados criado")
        self.desconecta_bd()
    def variaveis (self):
        self.Nome = self.Nome_entry.get()
        self.Cod = self.Cod_entry.get()
        self.Telefone = self.Telefone_entry.get()
        if self.estado.get() == "ESTADO":
           self.Estado = ""
        else:
            self.Estado = self.estado.get()
        if self.cidade.get() == "CIDADE":
           self.Cidade = ""
        else:
            self.Cidade = self.cidade.get()     
        self.Bairro = self.Bairro_entry.get()        
        self.Complemento = self.Complemento_entry.get()        
        self.E_mail = self.E_mail_entry.get()

        self.Nome1 = self.Nome1_entry.get()
        self.Cod1 = self.Cod1_entry.get()
        self.Telefone1 = self.Telefone1_entry.get()
        if self.estado1.get() == "ESTADO":
           self.Estado1 = ""
        else:
            self.Estado1 = self.estado1.get()
        if self.cidade1.get() == "CIDADE":
           self.Cidade1 = ""
        else:
            self.Cidade1 = self.cidade1.get()        
        self.Bairro1 = self.Bairro1_entry.get()        
        self.Complemento1 = self.Complemento1_entry.get()        
        self.E_mail1 = self.E_mail1_entry.get()

        self.Nome2 = self.Nome2_entry.get()
        self.Cod2 = self.Cod2_entry.get()
        self.Telefone2 = self.Telefone2_entry.get()        
        self.E_mail2 = self.E_mail2_entry.get()

        self.Nome3 = self.Nome3_entry.get()
        self.Cod3 = self.Cod3_entry.get()
        self.Telefone3 = self.Telefone3_entry.get()      
        self.E_mail3 = self.E_mail3_entry.get()

    def pode_cod(self):
        self.variaveis()
        lista = self.cursor.execute(f""" SELECT Cod FROM {self.usuario}""")
        cod = ''

        for i in lista:
            i = str(i)
            for c in range(len(i)):
                if i[c] != "'" and i[c] != "(" and i[c] != ")" and  i[c] != ",":
                    cod = cod + i[c]
            
            if cod == self.Cod:
                return False
            elif cod == self.Cod1:
                return False
        
        return True      
    #Funcao para um novo cadastro
      #Funcao para um novo cadastro
    def novo_cadastro(self):
        self.variaveis()
        self.conecta_bd()
        if self.Cod != "" and self.Nome != "":
            var = self.pode_cod()
            
            if var == True:
                self.cursor.execute(f"""INSERT INTO {self.usuario} (Cod, Nome, Telefone, Estado, Cidade, Bairro, Complemento, Email)
                                    VALUES (?, ?, ?, ?, ?, ?, ?, ?)""", ( self.Cod, self.Nome, self.Telefone, self.Estado, self.Cidade, self.Bairro, self.Complemento, self.E_mail))
                self.conn.commit()
                self.desconecta_bd()
                self.select_lista()
                self.limpa_tela()
                Label(self.Cadastro, text="Código já cadastrado", bg="dodgerblue", fg="dodgerblue").place(relx=0.82, rely=0.01)
            else:
                Label(self.Cadastro, text="Código já cadastrado", bg="dodgerblue", fg="red").place(relx=0.82, rely=0.01)
        else:
            msg = "Para realização do cadastro é obrigatório o preenchimento \ndas áreas 'Nome' e 'Codigo'"
            messagebox.showinfo("Aviso!!!", msg)
        self.desconecta_bd()
    #
    def select_lista (self):
        self.tabela_cadastrados.delete(*self.tabela_cadastrados.get_children())
        self.conecta_bd()
        lista = self.cursor.execute(f""" SELECT Cod, Nome, Telefone FROM {self.usuario} ORDER BY Nome ASC; """)

        for i in lista:
            self.tabela_cadastrados.insert("", END, values=i)
        
        self.desconecta_bd()
    def busca_cadastro (self):
        self.variaveis()
        self.tabela_cadastrados.delete(*self.tabela_cadastrados.get_children())
        self.conecta_bd()

        lista = self.cursor.execute(f""" SELECT Cod, Nome, Telefone, Estado, Cidade, Bairro, Complemento, Email FROM {self.usuario} ORDER BY Nome ASC; """)
        if self.Cod2_entry.get() != "":
            ###Busca por Codigo
            lista = self.cursor.execute(f""" SELECT Cod, Nome, Telefone, Estado, Cidade, Bairro, Complemento, Email FROM {self.usuario} WHERE Cod =  "{self.Cod2}";""")
        elif self.E_mail2_entry.get() != "":
            ###Busca por E-mail
            lista = self.cursor.execute(f""" SELECT Cod, Nome, Telefone FROM {self.usuario} WHERE Email =  "{self.E_mail2}";""")
        elif self.Telefone2_entry.get() != "":
            ###Busca por Telefone
            lista = self.cursor.execute(f""" SELECT Cod, Nome, Telefone FROM {self.usuario} WHERE Telefone =  "{self.Telefone2}";""")
        elif self.Nome2_entry.get() != "":
            ###Busca por Nome
            self.Nome2_entry.insert(END, '%')
            nome = self.Nome2_entry.get()
            self.cursor.execute(f""" SELECT Cod, Nome, Telefone FROM {self.usuario} WHERE Nome LIKE '%s' ORDER BY Nome ASC;""" % nome)
            lista = self.cursor.fetchall()

        for i in lista:
            self.tabela_cadastrados.insert("", END, values=i)

        self.limpa_tela()
        self.desconecta_bd()
    def duplo_click(self, event):
        self.limpa_telas()
        self.tabela_cadastrados.selection()

        for n in self.tabela_cadastrados.selection():
            col1, col2, col3 = self.tabela_cadastrados.item(n, 'values')

            Cod = col1

        self.conecta_bd()
        lista = self.cursor.execute(f""" SELECT Nome, Cod, Telefone, Estado, Cidade, Bairro, Complemento, Email FROM {self.usuario} WHERE Cod = '{Cod}' ; """)
        
        for i in lista:
            i = str(i)
            tam = len(i)
            var = 1
            nome = ""
            cod = ""
            tel = ""
            est = ""
            cid = ""
            bai = ""
            com = ""
            email = ""
            for c in range(tam):
                if c > 1:
                    if i[c] != "'":
                        if i[c] != ',':
                            if i[c-1] != ',' and c != tam -1:
                                if i[c] != "\n":    
                                    if var == 1:
                                        nome = nome + i[c]
                                    elif var == 2:
                                        cod = cod + i[c]    
                                    elif var == 3:
                                        tel = tel + i[c]
                                    elif var == 4:
                                        cid = cid + i[c]
                                    elif var == 5:
                                        est = est + i[c]
                                    elif var == 6:
                                        bai = bai + i[c]
                                    elif var == 7:
                                        com = com + i[c]
                                    elif var == 8:
                                        email = email + i[c]  
                    elif i[c-2] == ",":
                        var += 1

        self.Nome_entry.insert(END, nome)
        self.Cod_entry.insert(END, cod)
        self.Telefone_entry.insert(END, tel)
        if (cid != ""):
            self.estado.set(est)
        else:
            self.estado.set("ESTADO")
        if (cid != ""):
            self.cidade.set(cid)
        else:
            self.cidade.set("CIDADE")
        self.Bairro_entry.insert(END, bai)
        self.Complemento_entry.insert(END, com)
        self.E_mail_entry.insert(END, email)

        self.Nome1_entry.insert(END, nome)
        self.Cod1_entry.insert(END, cod)
        self.Telefone1_entry.insert(END, tel)
        if (cid != ""):
            self.estado.set(est)
        else:
            self.estado.set("ESTADO")
        if (cid != ""):
            self.cidade.set(cid)
        else:
            self.cidade.set("CIDADE")
        self.Bairro1_entry.insert(END, bai)
        self.Complemento1_entry.insert(END, com)
        self.E_mail1_entry.insert(END, email)
        
        self.Nome2_entry.insert(END, nome)
        self.Cod2_entry.insert(END, cod)
        self.Telefone2_entry.insert(END, tel)
        self.E_mail2_entry.insert(END, email)

        self.Nome3_entry.insert(END, nome)
        self.Cod3_entry.insert(END, cod)
        self.Telefone3_entry.insert(END, tel)
        self.E_mail3_entry.insert(END, email)

        self.desconecta_bd()
    def exclui_cadastro (self):
        self.variaveis()

        self.conecta_bd()

        if self.Cod3 == "":
            self.busca_cadastro()
            Label(self.Exclusão, text="Coloque o codigo do cadastro para exclui-lo", bg="dodgerblue", fg="red").place(relx=0.35, rely=0.01)
        else:
            ###Busca por Codigo
            self.cursor.execute(f"""DELETE FROM {self.usuario} WHERE Cod = '{self.Cod3}';""")
            self.conn.commit()
            self.limpa3_tela()
            self.select_lista()

        self.desconecta_bd()
    def altera_cadastro (self):
        self.variaveis()
        self.conecta_bd()
        var = self.pode_cod()
        
        if var == True:
            self.cursor.execute(f"""UPDATE {self.usuario} SET Nome = '{self.Nome1}', Telefone = '{self.Telefone1}', Estado = '{self.Estado1}', Cidade = '{self.Cidade1}', Bairro = '{self.Bairro1}', Complemento = '{self.Complemento1}', Email = '{self.E_mail1}' WHERE cod = '{self.Cod1}'""")
            self.conn.commit()
            self.desconecta_bd()
            self.select_lista()
            self.limpa1_tela()
            Label(self.Cadastro, text="Código já cadastrado", bg="dodgerblue", fg="dodgerblue").place(relx=0.82, rely=0.01)
        else:
            Label(self.Alteração, text="Código já cadastrado", bg="dodgerblue", fg="red").place(relx=0.82, rely=0.01)