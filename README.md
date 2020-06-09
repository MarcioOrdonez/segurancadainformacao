# Projeto Segurança da Informação

## Objetivo?
Projeto tem intuito de demonstrar modelagem de banco de dados ideal para um mercado se adequar com a LGPD, fazendo com que seja possível a exclusão de dados normais e sensiveis dos clientes. Por meio de uma aplicação que simule tal situação.

### Sistema de Agendamento para Salão de Cabelereiros
Usamos para exemplificar a criação de sistema de salão de cabeleireiro como cadastro de usuario, agendamento. O Principal objetivo é desmostrar como projetar o sistema para que o usuario possa excluir e gerenciar seus dados sem que interfira na integridade relacinal do banco de dados e não prejudique o funcionamento do sistema.
**Exemplo**
Nome | Telefone | Data do Agendamento | Valor
--- |--- |--- |---
Eduardo |12-34566789 | 01/06/20 | R$ 40,00
Anonimo|**Dado Deletado** | 01/06/20 | R$ 40,00

## O que é LGPD?
[![](http://img.youtube.com/vi/y7SamL2wYSc/0.jpg)](http://www.youtube.com/watch?v=y7SamL2wYSc "O que é LGPD?")

## Processo de Desenvolvimento
---

### Sprint 1
 - [x] Coletar boas idéias 
 - [x] Escolher melhores ferramentas
 - [x] Como planejar as strints
 - [x] Criar calendarios possiveis

### Sprint 2
- [x] Criar protóticos
- [x] Desmonstar ideias
- [x] Fazer Testes
- [x] Tarefa

## Instalação e Configuração do ambiente virtual

### Pré requisitos de instalação

Para executar o ambiente de desenvolvimento é necessario que tenha essa dependências abaixo: 

* Python 3.8
* virtualenv
* pip
* Flask


Abra o terminal de comando e execute os seguites comandos:

* Instalação do python 3\
`sudo apt-get install python3`

* Instalação do Pip, caso são possua instalado (pip é um sistema de gerenciamento de pacotes padrão da linguagem Python)\
 `sudo apt-get install python-pip`

* Instalação do Virtualenv (Criação de ambientes virtuais isolados)\
`pip install virtualenv`

* Criando uma virtualenv\
`virtualenv nome_da_virtualenv`

* Ativando a virtualenv\
`source nome_da_virtualenv/bin/activate`

* Instalando Flask\
`pip install flask`

* Intalando todas as depêndencias do projeto\
`pip install -r requirements.txt`

* Depois dos procedimentos, basta executar o projeto na IDE desejada e que interprete python

## Tecnologias utilizadas

* Python 
* Flask
* HTML e CSS
* MySQL

## Autores

* Marcio Ordonez 
* Eduardo Nunes 
* Thiago Dias
* Elias Fabiano
* Cauan Almeida



## Licença
Esse sistema e seu código fonte são livres para serem estudados e utilizados por quaisquer interessados que desejem entender mais sobre seu funcionamento


## Agradecimento
Professor e Orientador da disciplina de Segurança da Informação da Fatec São José dos Campos
