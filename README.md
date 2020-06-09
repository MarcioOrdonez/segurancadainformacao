# Projeto Segurança da Informação

## Objetivo?
Projeto tem intuito de demonstrar modelagem de banco de dados ideal para um mercado que se adeque com a LGPD, fazendo com que seja possível a exclusão de dados normais e sensiveis dos clientes. Por meio de uma aplicação que simule tal situação.

### Sistema de Agendamento para Salão de Cabelereiros
Usamos para exemplificar a criação de sistema de salão de cabeleireiro como cadastro de usuario, agendamento. O Principal objetivo é desmostrar como projetar o sistema para que o usuario possa excluir e gerenciar seus dados sem que interfira na integridade relacional do banco de dados e não prejudique o funcionamento do sistema.
**Exemplo**
Nome | Telefone | Data do Agendamento | Valor
--- |--- |--- |---
Eduardo |12-34566789 | 01/06/20 | R$ 40,00
Anonimo|**Dado Deletado** | 01/06/20 | R$ 40,00

## O que é LGBD?
[![](http://img.youtube.com/vi/y7SamL2wYSc/0.jpg)](http://www.youtube.com/watch?v=y7SamL2wYSc "O que é LGPD?")

## Processo de Desenvolvimento
---

### Sprint 1
 - [x] Coletar boas idéias 
 - [x] Escolher melhores ferramentas
 - [x] Como planejar as sprints
 - [x] Criar calendarios possiveis
 
### Sprint 2
- [x] Criar protótipos
- [x] Demonstar idéias
- [x] Fazer Testes
- [x] Tarefa

## Instalação e Configuração do ambiente virtual

### Pré requisitos de instalação

Para execultar o ambiente de desenvolvimento é necessário que tenha essa dependências abaixo: 

* python 3.8
* virtualenv
* pip
* Flask


Abra o terminal de comando e execute os seguitee comandos:

* Instalação do python 3.8
`sudo apt-get install python3`

* Instalação do Pip (pip é um sistema de gerenciamento de pacotes padrão)
 `sudo apt-get install python-pip`

* Instalação do Virtualenv (Controlador de dependências)
`pipx install virtualenv`

* Criando uma virtualenv 
`virtualenv nome_da_virtualenv`

* Ativando a virtualenv
`souce nome_da_virtualenv/bin/activate`

* Instalando Flask
`pip install flask`

* Intalando as depêndencias
`pip install -r requirements.txt` 

* Depois dos procedimentos basta executar o projeto em uma IDE desejada que interprete python

## Tecnologias Usadas

* Python 
* Flask
* HTML/CSS
* MySQL

## Autores 

* Marcio Ordonez 
* Eduardo Nunes 
* Thiago Dias
* Elias Fabiano
* Cauan Almeida



## Lincença 
Esse sistema tem seu código fonte livre para ser estudado e usado por qualquer pessoa.


## Agradecimento 
Professor e Orientador  Segurança da Informação da Fatec São José dos Campos
Eduardo Sakaue.
