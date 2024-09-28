# -*- coding: windows-1252 -*-

from service.serviceUser import forca_opcao, senha_len, verifica_idade, cadastro_usuario, login_usuario, \
    dados_cadastrados, verifica_email_cadastro, email_existe, printar_noticias, quiz_data, \
    moedas, buscar_valores, adicionar_moedas, conversar_com_chatbot, logging, verifica_usurio_index

import nltk
nltk.download('punkt')
nltk.download('punkt_tab')
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

exec(open('./service/serviceUser.py').read())

moedas_conversa = 0
moedas_perguntas = 0
invalido = 0
escolha_incio = forca_opcao("Digite 1 para se cadastrar ou 2 para fazer login: ", ['1', '2'])

while escolha_incio != '3':
    while escolha_incio == '1':
        print("Fa�a seu cadastro!")
        nome = input("Diga seu nome: ")
        senha = senha_len("Digite sua senha: ")
        endereco = input("Digite seu endere�o: ")
        email = input("Diga seu email: ")
        while not verifica_email_cadastro(email):
            logging.warning("Tentativa de cadastro com email inv�lido")
            email = input("Email inv�lido! Digite novamente: ")

        idade = input("Diga sua idade: ")
        while verifica_idade(idade) == 3:
            logging.warning(f"Input inv�lido para idade: {idade}")
            idade = input("Insira um n�mero: ")

        if not verifica_idade(idade):
            logging.error("Usu�rio menor de 18 anos tentando acessar o site.")
            raise Exception("Voc� deve ter mais de 18 anos para acessar o site!")

        cadastro_usuario(nome, senha, endereco, email, idade)
        logging.info(f"Usu�rio {nome} cadastrado com sucesso.")
        invalido = 0
        print('Voc� completou seu cadastro!')
        escolha_incio = '2'
        break

    while escolha_incio == '2':
        print("Fa�a seu login")
        try:
            email = input("Diga seu email: ")
            if not email_existe(email, dados_cadastrados):
                raise ValueError("Email n�o encontrado.")
        except ValueError as ve:
            logging.warning(f"Tentativa de login com email inv�lido: {email}")
            email = input("Email inv�lido! Digite novamente: ")
            email_existe(email, dados_cadastrados)

        senha = input("Digite sua senha: ")
        email = login_usuario(email, senha)
        if not email:
            logging.warning(f"Tentativa de login falhou para o email: {email}")
            escolha_incio = forca_opcao(
                "Credenciais inv�lidas!\nDigite 1 para se cadastrar ou 2 para fazer login novamente: ",
                ['1', '2'])
        else:
            logging.info(f"Usu�rio logado com sucesso: {email}")
            escolha_incio = '3'

try:
    indice = verifica_usurio_index(dados_cadastrados, email)
    logging.info(f"Usu�rio {email} acessou o sistema com sucesso.")
    print(f"Bem vindo {dados_cadastrados[indice]['nome']} a Formula-E!\n"
          f"Aqui voc� encontrar� quizes para se divertir e uma comunidade muito acolhedora para tirar d�vidas e "
          f"conversar!")
except Exception as e:
    logging.error(f"Erro ao tentar acessar o sistema: {e}")
    print(e)

escolha_site = forca_opcao("Home[Digite 1], Quizzes[Digite 2], Comunidade[Digite 3] ", ['1', '2', '3'])
while True:
    while escolha_site == '1':
        print("-" * 67)
        print(' ' * 30, 'Home')
        print("-" * 67)

        print(' ' * 28, 'Noticias')
        printar_noticias()

        try:
            moedas_usuario = buscar_valores(dados_cadastrados, 'moedas', email)
            print(f" Voc� tem {moedas_usuario} moedas")
        except Exception as e:
            logging.error(f"Erro ao buscar moedas para o usu�rio {email}: {e}")

        escolha_site = forca_opcao("Home[Digite 1], Quizzes[Digite 2], Comunidade[Digite 3] ", ['1', '2', '3'])

    while escolha_site == '2':
        print("-" * 67)
        print(' ' * 30, 'Quizzes', ' ' * 30)
        print("-" * 67)
        num_pergunta = 1
        indice_quiz = 0
        for data_quiz in quiz_data['questions']:
            print(f"{num_pergunta}� pergunta - {data_quiz['question']}")
            num_pergunta += 1
            opcoes = 1
            for opcao in data_quiz["options"]:
                print(f"{opcoes}) {opcao}")
                opcoes += 1
            resposta = int(forca_opcao(f"Digite a resposta: ", ['1', '2', '3', '4']))
            if data_quiz["options"][resposta - 1] in data_quiz['answer']:
                print("Voc� acertou! Ganhou 10 moedas!\n")
                moedas_perguntas += 10
            else:
                print("Voc� errou...\n")
            indice_quiz += 1

        try:
            adicionar_moedas(dados_cadastrados, email, moedas_perguntas)
            print(f"Parab�ns! Voc� ganhou {moedas_perguntas} moedas no total")
        except Exception as e:
            logging.error(f"Erro ao adicionar moedas para o usu�rio {email}: {e}")

        escolha_site = forca_opcao("Home[Digite 1], Quizzes[Digite 2], Comunidade[Digite 3] ", ['1', '2', '3'])

    while escolha_site == '3':
        print("-" * 67)
        print(' ' * 30, 'Comunity', ' ' * 30)
        print("-" * 67)
        print(' ' * 30, 'A cada msg vc ganha 1 ponto', ' ' * 30)

        # Crie uma inst�ncia do chatbot
        chatbot = ChatBot('Connect-E',
                          storage_adapter='chatterbot.storage.SQLStorageAdapter',
                          database_uri='sqlite:///database.sqlite3'
                          )

        # Treinador que usa o corpus de dados para treinamento
        trainer = ChatterBotCorpusTrainer(chatbot)

        # Treinar o chatbot com o corpus padr�o em portugu�s
        trainer.train("chatterbot.corpus.portuguese")
        moedas_conversa = 0

        try:
            moedas_conversa = conversar_com_chatbot(chatbot, moedas_conversa)
            adicionar_moedas(dados_cadastrados, email, moedas_conversa)
            print(f"Voc� ganhou {moedas_conversa} moedas")
        except Exception as e:
            logging.error(f"Erro no chatbot ou na adi��o de moedas: {e}")

        escolha_site = forca_opcao("Home[Digite 1], Quizzes[Digite 2], Comunidade[Digite 3] ", ['1', '2', '3'])