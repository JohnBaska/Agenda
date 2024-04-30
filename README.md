# Agenda

## Project Description

This project was made completely in python with the tkinter library. 

The project basically consists of something similar to a phone book, that with each new user regitered a new datebase is created to save your contacts together with a treeview (for improve the designer)

<!--⚠️ ATENÇÃO - Projeto em processo de atualização-->

## Configurções prévias

Para rodar esse projeto você precisa estar com o python baixado em seu computador

## Explicação do projeto

### Janela de login:

#### Aba cadastro:
+ Campos de preenchimento
  + Nome
  + Senha
+ Botões
  + Cadastrar
    + Serve para fazer o cadastro do usuário no banco de dados
    + Reinicia os campos de preenchimento

#### Aba logar:
+ Depois do usuário fazer o cadastro
+ Caampos de preenchimento:
  + Nome
  + Senha
+ Botões:
  + Logar
    + O programa procura (no banco de dados) o usuário e confirma a senha
    + Senha corrreta: 
      + Prompt de aviso: Login feito co suucesso
      + Criar um Banco de dados com o nome de usuário cadastrado para armazenar os cadastros feitos por aquele usuário
    + Senha incorreta 
      + Prompt de aviso: Cadastro não existe
      + Reinicia os campos de preenchimento

### Janela Principal

#### Aba Cadastrar:
+ Campos de preenchimento:
  + Nome - preenchimento obrigatório
  + Código (Para melhor identificação) - preenchimento obrigatório
  + E-mail
  + Telefone
  + Estado (Menu de opções)
  + Cidade (Menu de opções que depende do Estado)
  + Bairro
  + Complemento
+ Botões
  + OK
    + Serve para quando o campo do Estado for preenchido o Menu de opções de cidades ser alimentado com as cidades do Estado escolhido
  + Cadastrar
    + Serve para armazenar no banco de dados e mostra na tabala logo abaixo o novo cadastro (OBS.: O código tem que ser único e esclusivo daquele cadastro)
  + Limpar
    + Serve para limpar todos os campos da aba cadastrar

#### Aba Alterar
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

Pegar todos os cadastro, ordenar os nomes por ordem alfabetica e mostra todos os cadastros na tabela (semente Nome, Código e Telefone)
