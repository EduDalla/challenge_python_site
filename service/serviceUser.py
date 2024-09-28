# -*- coding: windows-1252 -*-

import re
import random
import time
import logging

# Configurando o logger
logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

moedas = 0
# regex para email
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
dados_cadastrados = [
    {'id': 1, 'nome': 'edu', 'senha': 'edu', 'endereco': 'educ4', 'email': 'edu', 'idade': 18, 'moedas': 100}]

quiz_data = {
    "questions": [
        {
            "question": "Qual foi o primeiro campeão da Fórmula E?",
            "options": [
                "Jean-Éric Vergne",
                "Sébastien Buemi",
                "Lucas di Grassi",
                "Nelson Piquet Jr."
            ],
            "answer": "Nelson Piquet Jr."
        },
        {
            "question": "Qual cidade sediou a primeira corrida da Fórmula E?",
            "options": [
                "Nova York",
                "Paris",
                "Pequim",
                "Tóquio"
            ],
            "answer": "Pequim"
        },
        {
            "question": "Quantas equipes participaram da primeira temporada da Fórmula E?",
            "options": [
                "8",
                "10",
                "12",
                "14"
            ],
            "answer": "12"
        },
        {
            "question": "Qual fabricante forneceu os primeiros motores elétricos para a Fórmula E?",
            "options": [
                "Audi",
                "BMW",
                "Renault",
                "Jaguar"
            ],
            "answer": "Renault"
        },
        {
            "question": "Qual piloto foi o primeiro a vencer duas vezes consecutivas o campeonato da Fórmula E?",
            "options": [
                "António Félix da Costa",
                "Jean-Éric Vergne",
                "Sam Bird",
                "Stoffel Vandoorne"
            ],
            "answer": "Jean-Éric Vergne"
        },
        {
            "question": "Qual equipe venceu o primeiro título de equipes na Fórmula E?",
            "options": [
                "Audi Sport ABT",
                "DS Techeetah",
                "Renault e.dams",
                "Mahindra Racing"
            ],
            "answer": "Renault e.dams"
        },
        {
            "question": "Quantas voltas completas tem uma corrida típica da Fórmula E?",
            "options": [
                "30",
                "45 minutos mais uma volta",
                "60 minutos",
                "25"
            ],
            "answer": "45 minutos mais uma volta"
        },
        {
            "question": "Qual cidade é a sede da FIA, o órgão que regula a Fórmula E?",
            "options": [
                "Paris",
                "Londres",
                "Genebra",
                "Mônaco"
            ],
            "answer": "Paris"
        },
        {
            "question": "Qual temporada da Fórmula E introduziu o 'Attack Mode'?",
            "options": [
                "Temporada 1",
                "Temporada 2",
                "Temporada 5",
                "Temporada 6"
            ],
            "answer": "Temporada 5"
        },
        {
            "question": "Qual piloto detém o recorde de mais vitórias em uma única temporada de Fórmula E?",
            "options": [
                "Sébastien Buemi",
                "Lucas di Grassi",
                "Mitch Evans",
                "Robin Frijns"
            ],
            "answer": "Sébastien Buemi"
        }
    ]
}

noticias = [
        {
            "data": '24 março 2023',
            "descricao": 'A criação de um circuito de Fórmula E',
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

# Função que faz cadastro do usuário, guardando as credenciais dele no "banco"
def cadastro_usuario(nome_usuario, senha_usuario, endereco_usuario, email_usuario, idade_usuario):
    id_usuario = random.randrange(100)
    usuario = {'id': id_usuario, 'nome': nome_usuario, 'senha': senha_usuario, 'endereco': endereco_usuario,
               'email': email_usuario, 'idade': idade_usuario, 'moedas': 0}
    dados_cadastrados.append(usuario)
    return True

# Função que faz login do usuário
def login_usuario(email_usuario, senha_usuario):
    for i in range(len(dados_cadastrados)):
        if email_usuario in dados_cadastrados[i]['email'] and senha_usuario in dados_cadastrados[i]['senha']:
            return email_usuario
    logger.warning(f"Tentativa de login falhou para o usuário: {email_usuario}")
    return False

# Função verifica se o email do cadastro existe ou está de acordo com o regex
def verifica_email_cadastro(email):
    if not re.fullmatch(regex, email):
        logger.warning(f"Formato de email inválido: {email}")
        return False
    if email_existe(email, dados_cadastrados):
        logger.warning(f"Email já existe: {email}")
        return False
    return email

# Função que verifica se o email do usuário existe
def email_existe(email, dados_cadastrados):
    for i in range(len(dados_cadastrados)):
        if dados_cadastrados[i]['email'] == email:
            return email
    logger.warning(f"Email não encontrado: {email}")
    return False

# Função que verifica se a senha é igual ou maior que 5
def senha_len(msg):
    senha = input(msg)
    while len(senha) < 5:
        logger.warning("Senha muito curta, deve ter 5 ou mais caracteres.")
        senha = input("Digite sua senha: ")
    return senha

# Função para verificar idade do usuário
def verifica_idade(idade):
    if not verifica_numero(idade):
        logger.warning(f"Idade inválida: {idade}")
        return 3
    if int(idade) < 18:
        return False
    return idade

# Função para verificar se o input é um número
def verifica_numero(num):
    try:
        numero = int(num)
        return numero
    except ValueError:
        logger.warning(f"Entrada inválida, não é um número: {num}")
        return False

# Função para receber a lista e buscar o elemento digitado
def meu_in(lista, buscar):
    for elem in lista:
        if elem == buscar:
            return True
    return False

# Função para adicionar moedas para o usuário selecionado
def adicionar_moedas(lista_discinario, email, moedas):
    try:
        index_usuario = verifica_usurio_index(lista_discinario, email)
        lista_discinario[index_usuario]['moedas'] += moedas
        return lista_discinario[index_usuario]['moedas']
    except Exception as e:
        logger.error(f"Erro ao adicionar moedas para o usuário {email}: {e}")
        raise

# Função para buscar valores específicos dentro do usuário
def buscar_valores(lista_discinario, buscar, email):
    try:
        index = verifica_usurio_index(lista_discinario, email)
        return lista_discinario[index][buscar]
    except Exception as e:
        logger.error(f"Erro desconhecido ao buscar valor para o usuário {email}: {e}")
        raise


# Função que verifica se o usuario existe e passa o index dele caso existir
def verifica_usurio_index(lista_discinario, email_usuario):
    for i in range(len(lista_discinario)):
        if lista_discinario[i]['email'] == email_usuario:
            return i
    logger.error(f"Usuário com email {email_usuario} não encontrado")
    raise Exception("Usuário não encontrado!")

# Função que força a opção do usuário
def forca_opcao(msg, lista_opcoes):
    msg_erro = ' '.join(lista_opcoes)
    msg_erro = f"Somente essas opções:\n{msg_erro}"
    opcao = input(msg)
    while not meu_in(lista_opcoes, opcao):
        logger.warning(f"Opção inválida: {opcao}. Somente essas opções são permitidas: {lista_opcoes}")
        print(msg_erro)
        opcao = input(msg)
    return opcao

# Função de printar as noticias da formula-e
def printar_noticias():
    for noticia in noticias:
        print(f"{noticia['data']}\n"
              f"{noticia['descricao']}\n"
              f"Para saber mais, visite {noticia['path']}\n")
        time.sleep(2.5)

# Função exterior que cria um chatbot interativo
def conversar_com_chatbot(chatbot, moedas_conversa):
    try:
        while True:
            # Recebe a entrada do usuário
            print("Digite 'sair' para encerrar\n")
            pergunta = input("Você: ")

            # Verifica se o usuário quer sair
            if pergunta.lower() == 'sair':
                print("Tchau! Até a próxima.")
                return moedas_conversa

            # Incrementa o contador de moedas de conversa
            moedas_conversa += 1

            # Gera uma resposta para a pergunta do usuário
            resposta = chatbot.get_response(pergunta)
            print("Formula-E:", resposta)

    except (KeyboardInterrupt, EOFError, SystemExit):
        logger.warning("Sessão do chatbot interrompida.")
        print("\nSessão encerrada. Até a próxima!")
        return moedas_conversa