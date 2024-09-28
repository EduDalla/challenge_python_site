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

# Fun��o que faz cadastro do usu�rio, guardando as credenciais dele no "banco"
def cadastro_usuario(nome_usuario, senha_usuario, endereco_usuario, email_usuario, idade_usuario):
    id_usuario = random.randrange(100)
    usuario = {'id': id_usuario, 'nome': nome_usuario, 'senha': senha_usuario, 'endereco': endereco_usuario,
               'email': email_usuario, 'idade': idade_usuario, 'moedas': 0}
    dados_cadastrados.append(usuario)
    return True

# Fun��o que faz login do usu�rio
def login_usuario(email_usuario, senha_usuario):
    for i in range(len(dados_cadastrados)):
        if email_usuario in dados_cadastrados[i]['email'] and senha_usuario in dados_cadastrados[i]['senha']:
            return email_usuario
    logger.warning(f"Tentativa de login falhou para o usu�rio: {email_usuario}")
    return False

# Fun��o verifica se o email do cadastro existe ou est� de acordo com o regex
def verifica_email_cadastro(email):
    if not re.fullmatch(regex, email):
        logger.warning(f"Formato de email inv�lido: {email}")
        return False
    if email_existe(email, dados_cadastrados):
        logger.warning(f"Email j� existe: {email}")
        return False
    return email

# Fun��o que verifica se o email do usu�rio existe
def email_existe(email, dados_cadastrados):
    for i in range(len(dados_cadastrados)):
        if dados_cadastrados[i]['email'] == email:
            return email
    logger.warning(f"Email n�o encontrado: {email}")
    return False

# Fun��o que verifica se a senha � igual ou maior que 5
def senha_len(msg):
    senha = input(msg)
    while len(senha) < 5:
        logger.warning("Senha muito curta, deve ter 5 ou mais caracteres.")
        senha = input("Digite sua senha: ")
    return senha

# Fun��o para verificar idade do usu�rio
def verifica_idade(idade):
    if not verifica_numero(idade):
        logger.warning(f"Idade inv�lida: {idade}")
        return 3
    if int(idade) < 18:
        return False
    return idade

# Fun��o para verificar se o input � um n�mero
def verifica_numero(num):
    try:
        numero = int(num)
        return numero
    except ValueError:
        logger.warning(f"Entrada inv�lida, n�o � um n�mero: {num}")
        return False

# Fun��o para receber a lista e buscar o elemento digitado
def meu_in(lista, buscar):
    for elem in lista:
        if elem == buscar:
            return True
    return False

# Fun��o para adicionar moedas para o usu�rio selecionado
def adicionar_moedas(lista_discinario, email, moedas):
    try:
        index_usuario = verifica_usurio_index(lista_discinario, email)
        lista_discinario[index_usuario]['moedas'] += moedas
        return lista_discinario[index_usuario]['moedas']
    except Exception as e:
        logger.error(f"Erro ao adicionar moedas para o usu�rio {email}: {e}")
        raise

# Fun��o para buscar valores espec�ficos dentro do usu�rio
def buscar_valores(lista_discinario, buscar, email):
    try:
        index = verifica_usurio_index(lista_discinario, email)
        return lista_discinario[index][buscar]
    except Exception as e:
        logger.error(f"Erro desconhecido ao buscar valor para o usu�rio {email}: {e}")
        raise


# Fun��o que verifica se o usuario existe e passa o index dele caso existir
def verifica_usurio_index(lista_discinario, email_usuario):
    for i in range(len(lista_discinario)):
        if lista_discinario[i]['email'] == email_usuario:
            return i
    logger.error(f"Usu�rio com email {email_usuario} n�o encontrado")
    raise Exception("Usu�rio n�o encontrado!")

# Fun��o que for�a a op��o do usu�rio
def forca_opcao(msg, lista_opcoes):
    msg_erro = ' '.join(lista_opcoes)
    msg_erro = f"Somente essas op��es:\n{msg_erro}"
    opcao = input(msg)
    while not meu_in(lista_opcoes, opcao):
        logger.warning(f"Op��o inv�lida: {opcao}. Somente essas op��es s�o permitidas: {lista_opcoes}")
        print(msg_erro)
        opcao = input(msg)
    return opcao

# Fun��o de printar as noticias da formula-e
def printar_noticias():
    for noticia in noticias:
        print(f"{noticia['data']}\n"
              f"{noticia['descricao']}\n"
              f"Para saber mais, visite {noticia['path']}\n")
        time.sleep(2.5)

# Fun��o exterior que cria um chatbot interativo
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
            print("Formula-E:", resposta)

    except (KeyboardInterrupt, EOFError, SystemExit):
        logger.warning("Sess�o do chatbot interrompida.")
        print("\nSess�o encerrada. At� a pr�xima!")
        return moedas_conversa