import re
import random

# regex para email
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
dados_cadastrados = [
    {'id': 1, 'nome': 'edu', 'senha': 'edu123', 'endereco': 'educ4', 'email': 'teste', 'idade': 18}]
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


def cadastro_usuario(nome_usuario, senha_usuario, endereco_usuario, email_usuario, idade_usuario):
    id_usuario = random.randrange(100)

    usuario = {'id': id_usuario, 'nome': nome_usuario, 'senha': senha_usuario, 'endereco': endereco_usuario,
               'email': email_usuario, 'idade': idade_usuario}
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
        print("A senha deve ter 5 ou mais caractéres")
        senha = input("Digite sua senha: ")
    return senha


def verifica_idade(idade):
    while not verifica_numero(idade):
        return 3
    if int(idade) < 18:
        return False
    return idade


# verifica se o input é um número
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


def meu_index_dicionario(lista_discinario, email_usuario):
    for i in range(len(lista_discinario)):
        if lista_discinario[i]['email'] == email_usuario:
            return i
    raise Exception("Usuário não encontrado!")


# força a opção do usuário
def forca_opcao(msg, lista_opcoes):
    msg_erro = ' '.join(lista_opcoes)
    msg_erro = f"Somente essas opcoes:\n{msg_erro}"
    opcao = input(msg)
    while not meu_in(lista_opcoes, opcao):
        print(msg_erro)
        opcao = input(msg)
    return opcao
