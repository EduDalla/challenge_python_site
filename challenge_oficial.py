from service.serviceUser import forca_opcao, senha_len, verifica_idade, cadastro_usuario, login_usuario, \
    verifica_email_lista, dados_cadastrados, verifica_email_cadastro, email_existe, printar_noticias, quiz_data, \
    moedas, buscar_valores, adicionar_moedas

exec(open('./service/serviceUser.py').read())

moedas_perguntas = 0
invalido = 0
escolha_incio = forca_opcao("Digite 1 para se cadastrar ou 2 para fazer login: ", ['1', '2'])
while escolha_incio != '3':
    while escolha_incio == '1':
        print("Faça seu cadastro!")
        nome = input("Diga seu nome: ")
        senha = senha_len("Digite sua senha: ")
        endereco = input("Digite seu endereço: ")
        email = input("Diga seu email: ")
        while not verifica_email_cadastro(email):
            email = input("Email inválido! Digite novamente: ")

        idade = input("Diga sua idade: ")
        while verifica_idade(idade) == 3:
            idade = input("Insira um número: ")

        if not verifica_idade(idade):
            raise Exception("Você deve ter mais de 18 anos para acessar o site!")

        cadastro_usuario(nome, senha, endereco, email, idade)
        invalido = 0
        print('Você completou seu cadastro!')
        escolha_incio = '2'
        break

    while escolha_incio == '2':
        print("Faça seu login")
        try:
            email = input("Diga seu email: ")
            email_existe(email)
        except:
            email = input("Email inválido! Digite novamente: ")
            email_existe(email)
        senha = input("Digite sua senha: ")
        email = login_usuario(email, senha)
        if not email:
            escolha_incio = forca_opcao(
                "Credenciais inválidas!\nDigite 1 para se cadastrar ou 2 para fazer login novamente: ",
                ['1', '2'])
        else:
            escolha_incio = '3'

try:
    indice = verifica_email_lista(dados_cadastrados, email)
    print(f"Bem vindo {dados_cadastrados[indice]['nome']} a Formula-E!\n"
          f"Aqui você encontrará quizes para se divertir e uma comunidade muito acolhedora para tirar dúvidas e "
          f"conversar!")
except Exception as e:
    print(e)

escolha_site = forca_opcao("Home[Digite 1], Quizzes[Digite 2], Comunidade[Digite 3] ", ['1', '2', '3'])
while True:
    while escolha_site == '1':
        print("-" * 67)
        print(' ' * 30, 'Home')
        print("🔵" * 30)

        print(' ' * 28, 'Noticias')
        printar_noticias()
        
        escolha_site = forca_opcao("Home[Digite 1], Quizzes[Digite 2], Comunidade[Digite 3] ", ['1', '2', '3'])

    while escolha_site == '2':
        print("-" * 67)
        print(' ' * 30, 'Quizzes', ' ' * 30)
        print("🔵" * 30)
        num_pergunta = 1
        indice_quiz = 0
        for data_quiz in quiz_data['questions']:
            print(f"{num_pergunta}º pergunta - {data_quiz['question']}")
            num_pergunta += 1
            opcoes = 1
            for opcao in data_quiz["options"]:
                print(f"{opcoes}) {opcao}")
                opcoes += 1
            resposta = int(forca_opcao(f"Digite a resposta: ", ['1', '2', '3', '4']))
            if data_quiz["options"][resposta - 1] in data_quiz['answer']:
                print("Você acertou! Ganhou 10 moedas!")
                moedas_perguntas += 10
            else:
                print("Você errou...")
            indice_quiz += 1

        adicionar_moedas(dados_cadastrados, email, moedas_perguntas)
        print(buscar_valores(dados_cadastrados, 'moedas', email))

        print(f"Parabéns! Você ganhou {moedas_perguntas} moedas")
        escolha_site = forca_opcao("Home[Digite 1], Quizzes[Digite 2], Comunidade[Digite 3] ", ['1', '2', '3'])

    while escolha_site == '3':
        print("-" * 67)
        print(' ' * 30, 'Comunity', ' ' * 30)
        print("🔵" * 30)
        print(' ' * 30, 'A cada msg vc ganha 1 ponto', ' ' * 30)
        escolha_site = forca_opcao("Home[Digite 1], Quizzes[Digite 2], Comunidade[Digite 3] ", ['1', '2', '3'])
