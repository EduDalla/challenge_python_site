# -*- coding: windows-1252 -*-

import re
import random
import time
import logging
# Configurando o logger
logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

moedas = 0
# regex para email
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
dados_cadastrados = [
    {'id': 1, 'nome': 'edu', 'senha': 'edu', 'endereco': 'educ4', 'email': 'edu', 'idade': 18, 'moedas': 100}]

quiz_data = {
    "questions": [
        {
            "question": "Qual foi o primeiro campe�o da F�rmula E?",
            "options": [
                "Jean-�ric Vergne",
                "S�bastien Buemi",
                "Lucas di Grassi",
                "Nelson Piquet Jr."
            ],
            "answer": "Nelson Piquet Jr."
        },
        {
            "question": "Qual cidade sediou a primeira corrida da F�rmula E?",
            "options": [
                "Nova York",
                "Paris",
                "Pequim",
                "T�quio"
            ],
            "answer": "Pequim"
        },
        {
            "question": "Quantas equipes participaram da primeira temporada da F�rmula E?",
            "options": [
                "8",
                "10",
                "12",
                "14"
            ],
            "answer": "12"
        },
        {
            "question": "Qual fabricante forneceu os primeiros motores el�tricos para a F�rmula E?",
            "options": [
                "Audi",
                "BMW",
                "Renault",
                "Jaguar"
            ],
            "answer": "Renault"
        },
        {
            "question": "Qual piloto foi o primeiro a vencer duas vezes consecutivas o campeonato da F�rmula E?",
            "options": [
                "Ant�nio F�lix da Costa",
                "Jean-�ric Vergne",
                "Sam Bird",
                "Stoffel Vandoorne"
            ],
            "answer": "Jean-�ric Vergne"
        },
        {
            "question": "Qual equipe venceu o primeiro t�tulo de equipes na F�rmula E?",
            "options": [
                "Audi Sport ABT",
                "DS Techeetah",
                "Renault e.dams",
                "Mahindra Racing"
            ],
            "answer": "Renault e.dams"
        },
        {
            "question": "Quantas voltas completas tem uma corrida t�pica da F�rmula E?",
            "options": [
                "30",
                "45 minutos mais uma volta",
                "60 minutos",
                "25"
            ],
            "answer": "45 minutos mais uma volta"
        },
        {
            "question": "Qual cidade � a sede da FIA, o �rg�o que regula a F�rmula E?",
            "options": [
                "Paris",
                "Londres",
                "Genebra",
                "M�naco"
            ],
            "answer": "Paris"
        },
        {
            "question": "Qual temporada da F�rmula E introduziu o 'Attack Mode'?",
            "options": [
                "Temporada 1",
                "Temporada 2",
                "Temporada 5",
                "Temporada 6"
            ],
            "answer": "Temporada 5"
        },
        {
            "question": "Qual piloto det�m o recorde de mais vit�rias em uma �nica temporada de F�rmula E?",
            "options": [
                "S�bastien Buemi",
                "Lucas di Grassi",
                "Mitch Evans",
                "Robin Frijns"
            ],
            "answer": "S�bastien Buemi"
        }
    ]
}

noticias = [
        {
            "data": '24 mar�o 2023',
            "descricao": 'A cria��o de um circuito de F�rmula E',
            "path": 'https://www.fiaformulae.com/pt-br/news/17969'
        },
        {
            "data": '30 junho 2024',
            "descricao": 'Da Costa makes it three wins in a row after sensational Portland showdown',
            "path": 'https://www.fiaformulae.com/pt-br/news/502496'
        },
        {
            "data": '24 julho 2024',
            "descricao": 'Rowland pride at targets "more than met" after maiden home win',
            "path": 'https://www.fiaformulae.com/pt-br/news/504373'
        },
        {
            "data": '21 julho 2024',
            "descricao": "Porsche's Pascal Wehrlein races through the drama to seal Formula E Drivers' World Championship...",
            "path": 'https://www.fiaformulae.com/pt-br/news/504132' 
        }
    ]



def cadastro_usuario(nome_usuario, senha_usuario, endereco_usuario, email_usuario, idade_usuario):
    id_usuario = random.randrange(100)

    usuario = {'id': id_usuario, 'nome': nome_usuario, 'senha': senha_usuario, 'endereco': endereco_usuario,
               'email': email_usuario, 'idade': idade_usuario, 'moedas': 0}
    dados_cadastrados.append(usuario)
    return True


def login_usuario(email_usuario, senha_usuario):
    for i in range(len(dados_cadastrados)):
        if email_usuario in dados_cadastrados[i]['email'] and senha_usuario in dados_cadastrados[i]['senha']:
            return email_usuario
    return False


def verifica_email_cadastro(email):
    while not re.fullmatch(regex, email) or email_existe(email):
        return False

    return email


def email_existe(email):
    for i in range(len(dados_cadastrados)):
        if dados_cadastrados[i]['email'] == email:
            return email

    return False


def senha_len(msg):
    senha = input(msg)
    while len(senha) < 5:
        print("A senha deve ter 5 ou mais caract�res")
        senha = input("Digite sua senha: ")
    return senha


def verifica_idade(idade):
    while not verifica_numero(idade):
        return 3
    if int(idade) < 18:
        return False
    return idade


# verifica se o input � um n�mero
def verifica_numero(num):
    try:
        numero = int(num)
        return numero
    except ValueError:
        return False


# recebe a lista e busca o elemento digitado
def meu_in(lista, buscar):
    for elem in lista:
        if elem == buscar:
            return True
    return False


# procura index do elemento
def meu_index(lista, buscar):
    for i in range(len(lista)):
        if lista[i] == buscar:
            return i
    return False


def adicionar_moedas(lista_discinario, email, moedas):
    try:
        index_usuario = verifica_usurio_index(lista_discinario, email)
        lista_discinario[index_usuario]['moedas'] += moedas
        return lista_discinario[index_usuario]['moedas']
    except:
        raise Exception("Valor n�o encontrado!")


def buscar_valores(lista_discinario, buscar, email):
    try:
        index = verifica_usurio_index(lista_discinario, email)
        return lista_discinario[index][buscar]
    except:
        raise Exception("Valor n�o encontrado!")


def verifica_usurio_index(lista_discinario, email_usuario):
    for i in range(len(lista_discinario)):
        if lista_discinario[i]['email'] == email_usuario:
            return i
    raise Exception("Usu�rio n�o encontrado!")


def verifica_email_lista(lista_discinario, email_usuario):
    for i in range(len(lista_discinario)):
        if lista_discinario[i]['email'] == email_usuario:
            return i
    raise Exception("Usu�rio n�o encontrado!")


# for�a a op��o do usu�rio
def forca_opcao(msg, lista_opcoes):
    msg_erro = ' '.join(lista_opcoes)
    msg_erro = f"Somente essas opcoes:\n{msg_erro}"
    opcao = input(msg)
    while not meu_in(lista_opcoes, opcao):
        print(msg_erro)
        opcao = input(msg)
    return opcao


def printar_noticias():
    for noticia in noticias:
        print(f"{noticia['data']}\n"
              f"{noticia['descricao']}\n"
              f"Para saber mais, visite {noticia['path']}\n")
        time.sleep(2.5)


def conversar_com_chatbot(chatbot, moedas_conversa):
    try:
        while True:
            # Recebe a entrada do usu�rio
            print("Digite 'sair' para encerrar\n")
            pergunta = input("Voc�: ")

            # Verifica se o usu�rio quer sair
            if pergunta.lower() == 'sair':
                print("Tchau! At� a pr�xima.")
                return moedas_conversa

            # Incrementa o contador de moedas de conversa
            moedas_conversa += 1

            # Gera uma resposta para a pergunta do usu�rio
            resposta = chatbot.get_response(pergunta)
            print("Chatbot:", resposta)

    except (KeyboardInterrupt, EOFError, SystemExit):
        print("\nSess�o encerrada. At� a pr�xima!")
        return moedas_conversa

