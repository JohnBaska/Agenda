# Agenda

## Project Description

This project was made completely in python with the tkinter library. 

The project basically consists of something similar to a phone book, that with each new user regitered a new datebase is created to save your contacts together with a treeview (for improve the designer)

<!--⚠️ ATENÇÃO - Projeto em processo de atualização-->

## Previous settings

For run this project you need to be with the python installed in your computer.

## Project explication

### Login window: 

#### "Cadastrar" Tab:
<div>
  <img src="Assets/Login_Cadastrar.png"/>
</div>

+ Fields of filling:
  + "Nome";
  + "Senha";
+ Buttons:
  + "Cadastrar"
    + It made the new user registration in datebase;
    + Reset the fields;

#### "Logar" Tab:
<div>
  <img src="Assets/Login_Logar.png"/>
</div>

+ After of the new user registration
+ Fields of filling:
  + "Nome"
  + "Senha"
+ Buttons:
  + "Logar"
    + The program search (in the datebase) the user and confirm password;
    + Correct password: 
      + Warning prompt: "Login feito com sucesso";
      + It's created a datebase with user name registered. For to save the registers made by that user;
    + Incorrect password: 
      + Warning prompt: "Cadastro não existe";
      + Reset fields;

### Janela Principal

#### Aba Cadastrar:
<div>
  <img src="Assets/Agenda-de-Contatos_Cadastrar.png" width="80%"/>
</div>

+ Fields of filling:
  + "Nome" - mandatory filling
  + "Código" (For it improves identification) - mandatory filling
  + "E-mail"
  + "Telefone"
  + "Estado" (options main)
  + "Cidade" (options main that depend on the Estado)
  + "Bairro"
  + "Complemento"
+ Buttons
  + "OK"
    + It fill the field "Cidade" it according to the state chosen by the user
  + "Cadastrar"
    + Serve para armazenar no banco de dados e mostra na tabala logo abaixo o novo cadastro (OBS.: O código tem que ser único e esclusivo daquele cadastro)
  + Limpar
    + Serve para limpar todos os campos da aba cadastrar
  + 

#### Aba Alterar
<div>
  <img src="Assets/Agenda-de-Contatos_Alterar.png" width="80%"/>
</div>

Para Utilização dessa aba Você deverá fazer a escolha de um cadastro pré-feito na Lista que fica logo abaixo e dar um duplo click para preencher automáticamente todos os campos com o cadastro ao qual você deseja alterar algum dado
+ Campos de preenchimento:
  + Nome
  + Código (Para melhor identificação)
  + E-mail
  + Telefone
  + Estado (Menu de opções)
  + Cidade (Menu de opções que depende do Estado)
  + Bairro
  + Complemento
+ Botões
  + OK
    + Serve para quando o campo do Estado for preenchido o Menu de opções de cidades ser alimentado com as cidades do Estado escolhido
  + Alterar
    + Serve para armazenar no banco de dados e mostra na tabala logo abaixo As alterações que você no cadastro (OBS.: O código tem que ser único e esclusivo daquele cadastro)
  + Limpar
    + Serve para limpar todos os campos da aba Alterar

#### Aba Buscar
<div>
  <img src="Assets/Agenda-de-Contatos_Buscar.png" width="80%"/>
</div>

+ Campos de preenchimento:
  + Nome 
  + Código (Para melhor identificação) 
  + E-mail
  + Telefone
+ Botões
  + Reiniciar
    + Server para reiniciar a tabela abaixo apos uma busca
  + Buscar
    + Serve para buscar no banco de dados os cadastros que tem as informações preenchidas pelo usuário e mostra na tabela abaixo
  + Limpar
    + Serve para limpar todos os campos da aba Buscar

#### Aba Excluir
<div>
  <img src="Assets/Agenda-de-Contatos_Excluir.png" width="80%"/>
</div>

+ Campos de preenchimento:
  + Nome 
  + Código (Para melhor identificação) 
  + E-mail
  + Telefone
+ Botões
  + Excluir
    + Serve para buscar no banco de dados os cadastros que tem as informações preenchidas pelo usuário e mostra na tabela abaixo e se o campo Codigo estiver preenchido o cadastro é apagado
  + Limpar
    + Serve para limpar todos os campos da aba Buscar

#### Tabela
<div>
  <img src="Assets/Agenda-de-Contatos_Lista.png" width="80%"/>
</div>

Pegar todos os cadastro, ordenar os nomes por ordem alfabetica e mostra todos os cadastros na tabela (semente Nome, Código e Telefone)
