# -*- coding: windows-1252 -*-

from service.serviceUser import forca_opcao, senha_len, verifica_idade, cadastro_usuario, login_usuario, \
    verifica_email_lista, dados_cadastrados, verifica_email_cadastro, email_existe, printar_noticias, quiz_data, \
    moedas, buscar_valores, adicionar_moedas, conversar_com_chatbot, logging

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
            email = input("Email inv�lido! Digite novamente: ")

        idade = input("Diga sua idade: ")
        while verifica_idade(idade) == 3:
            idade = input("Insira um n�mero: ")

        if not verifica_idade(idade):
            raise Exception("Voc� deve ter mais de 18 anos para acessar o site!")

        cadastro_usuario(nome, senha, endereco, email, idade)
        invalido = 0
        print('Voc� completou seu cadastro!')
        escolha_incio = '2'
        break

    while escolha_incio == '2':
        print("Fa�a seu login")
        try:
            email = input("Diga seu email: ")
            email_existe(email, dados_cadastrados)
        except:
            email = input("Email inv�lido! Digite novamente: ")
            email_existe(email, dados_cadastrados)
        senha = input("Digite sua senha: ")
        email = login_usuario(email, senha)
        if not email:
            escolha_incio = forca_opcao(
                "Credenciais inv�lidas!\nDigite 1 para se cadastrar ou 2 para fazer login novamente: ",
                ['1', '2'])
        else:
            escolha_incio = '3'

try:
    indice = verifica_email_lista(dados_cadastrados, email)
    print(f"Bem vindo {dados_cadastrados[indice]['nome']} a Formula-E!\n"
          f"Aqui voc� encontrar� quizes para se divertir e uma comunidade muito acolhedora para tirar d�vidas e "
          f"conversar!")
except Exception as e:
    print(e)

escolha_site = forca_opcao("Home[Digite 1], Quizzes[Digite 2], Comunidade[Digite 3] ", ['1', '2', '3'])
while True:
    while escolha_site == '1':
        print("-" * 67)
        print(' ' * 30, 'Home')
        print("-" * 67)

        print(' ' * 28, 'Noticias')
        printar_noticias()

        print(f" Voc� tem {buscar_valores(dados_cadastrados, 'moedas', email)} moedas")

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
                print("Voc� acertou! Ganhou 10 moedas!")
                moedas_perguntas += 10
            else:
                print("Voc� errou...")
            indice_quiz += 1

        adicionar_moedas(dados_cadastrados, email, moedas_perguntas)

        print(f"Parab�ns! Voc� ganhou {moedas_perguntas} moedas")
        escolha_site = forca_opcao("Home[Digite 1], Quizzes[Digite 2], Comunidade[Digite 3] ", ['1', '2', '3'])

    while escolha_site == '3':
        print("-" * 67)
        print(' ' * 30, 'Comunity', ' ' * 30)
        print("-" * 67)
        print(' ' * 30, 'A cada msg vc ganha 1 ponto', ' ' * 30)
        # Crie uma inst�ncia do chatbot
        chatbot = ChatBot('Connect-E')

        # Treinador que usa o corpus de dados para treinamento
        trainer = ChatterBotCorpusTrainer(chatbot)

        # Treinar o chatbot com o corpus padr�o em portugu�s
        trainer.train("chatterbot.corpus.portuguese")
        moedas_conversa = 0
        print("Digite 'sair' para encerrar a conversa.\n")
        moedas_conversa = conversar_com_chatbot(chatbot, moedas_conversa)

        adicionar_moedas(dados_cadastrados, email, moedas_conversa)

        print(f"Voc� ganhou {moedas_conversa} moedas")
        escolha_site = forca_opcao("Home[Digite 1], Quizzes[Digite 2], Comunidade[Digite 3] ", ['1', '2', '3'])
