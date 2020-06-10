# Projeto Segurança da Informação

## Objetivo?
Projeto tem intuito de demonstrar modelagem de banco de dados ideal para um mercado que se adeque com a LGPD, fazendo com que seja possível a exclusão de dados normais e sensiveis dos clientes. Por meio de uma aplicação que simule tal situação.

### Sistema de Agendamento para Salão de Cabelereiros
Usamos para exemplificar a criação de sistema de salão de cabeleireiro como cadastro de usuario, agendamento. O Principal objetivo é desmostrar como projetar o sistema para que o usuario possa excluir e gerenciar seus dados sem que interfira na integridade relacional do banco de dados e não prejudique o funcionamento do sistema.
**Exemplo**
id |Nome | Telefone | Data do Agendamento | Valor
---|--- |--- |--- |---
1|Eduardo |12-34566789 | 01/06/20 | R$ 40,00
2|CRIPTOGRAFADO|CRIPTOGRAFADO| 01/06/20 | R$ 40,00

## Solução utilizada
A solução utilizada para desse problema foi utilização de criptografia assimetrica, que se trata de uma criptografia que utiliza duas chaves uma publica e uma privada, sendo a publica a chave utilizada para criptografar os dados e a privada para descriptografar o mesmo.
## O que é LGPD?
[![](http://img.youtube.com/vi/y7SamL2wYSc/0.jpg)](http://www.youtube.com/watch?v=y7SamL2wYSc "O que é LGPD?")

## Processo de Desenvolvimento
---

### Sprint 1
 - [x] Inicio da modelagem do banco de dados 
 - [x] Criação da base e estrutura MVC
 - [x] wireframes das paginas

### Sprint 2
- [x] Criação de controllers responsaveis pelo login e autenticação
- [x] Mudanças no banco de dados
- [x] Criação de bases HTML para as paginas
### Sprint 3
- [x] Metodos de anonimização de usuarios quando deletados
- [x] Controllers de agendamentos serviços e usuarios
- [x] Ajustes no modelo do banco de dados
### Sprint 4
- [x] Novo modelo do banco de dados
- [x] Novo banco de dados para chave privada
- [x] Criação de modulo de criptografia
- [x] Utilização do modulo de criptografia no controller de usuarios
## Instalação e Configuração do ambiente virtual


### Tecnologias utilizadas

* python 3.8
* virtualenv
* pip
* Flask
* HTML e CSS
* MySQL

## Instalação
Abra o terminal de comando e execute os seguites comandos:

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
