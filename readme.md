
# 📋 Challenge Python CONNECT-E

Este projeto simula nosso sistema que criamos para a Formula-E. Este código implementa todas as funcionalidades vistas na aula de python!

## 🚀 Funcionalidades

O sistema possui as seguintes funcionalidades principais:

1. **Cadastro de Usuários**: Permite o cadastro de novos usuários com informações como nome, senha, endereço, e-mail e idade.
2. **Login de Usuários**: Valida os dados de login (nome de usuário e senha) para acessar o sistema.
3. **Validação de Idade**: Verifica se a idade do usuário é maior ou igual a 18 anos.
4. **Validação de E-mail**: Verifica se o e-mail do usuário está em um formato válido e se já está cadastrado no sistema.
5. **Gerenciamento de Moedas**: Adiciona moedas à conta do usuário ou verifica a quantidade de moedas disponíveis.
6. **Busca de Valores**: Busca valores específicos dos usuários cadastrados, como idade, moedas, entre outros.
7. **Conversa com chatbot**: Conversa com o um gerador aleatório de mensagens.

## 🛠 Tecnologias Utilizadas

- **Python 3.8**: Linguagem de programação usada para implementar as funcionalidades.
- **Unittest**: Biblioteca padrão do Python para criação de testes unitários.
- **Regex**: Usado para validação de e-mails e outros padrões.
- **Random**: Usado para gerar IDs únicos para novos usuários.
- **Logging**: Utilizado para registrar eventos, avisos e erros que ocorrem durante a execução do código.
- **Time**: Utilizado para pausar a execução de algumas funções (como a exibição de notícias).
- **NLTK**: Biblioteca usada para processamento de linguagem natural.
- **ChatterBot**: Biblioteca usada para criar chatbots.
Caso tiver alguma difuculdade em instalar a biblioteca do ChatterBot, acesse a documentação oficial deles: 
[Clique aqui](https://chatterbot.readthedocs.io/en/stable/)

### Bibliotecas do Python Usadas

- **`re`**: Para a criação de expressões regulares (regex), ajudando na validação dos e-mails.
- **`random`**: Para gerar IDs aleatórios durante o cadastro de usuários.
- **`time`**: Para introduzir pequenas pausas na exibição das notícias, simulando uma interface de usuário mais amigável.
- **`logging`**: Para gerar logs de erros e avisos durante o processo de cadastro, login e outras interações com o sistema.
- **`nltk`**: Para processamento de linguagem natural.
- **`chatterbot`**: Para criar e treinar chatbots.

## 📁 Estrutura do Projeto

```
/
├── service/
│   └── serviceUser.py  # Implementação das funções de serviço para cadastro e login de usuários
├── tests/
│   └── challengeTest.py  # Testes unitários para validação das funcionalidades
│
├── challenge_oficial.py # Código principal (main)
│
└── README.md  # Documentação do projeto
```

## ✅ Funcionalidades Testadas

Os testes unitários estão localizados no arquivo `test_serviceUser.py` e cobrem as seguintes funcionalidades:

1. **Verificação de E-mail** (`verifica_email_cadastro`): Testa se o formato do e-mail é válido e se já existe um e-mail igual cadastrado.
2. **Login de Usuário** (`login_usuario`): Garante que o usuário só pode acessar o sistema se o nome e a senha estiverem corretos.
3. **Verificação de Idade** (`verifica_idade`): Garante que apenas usuários maiores de idade (18+) possam ser cadastrados.
4. **Existência de E-mail** (`email_existe`): Verifica se o e-mail já está cadastrado no sistema.
5. **Validação de Número** (`verifica_numero`): Garante que os dados de idade ou moedas sejam números válidos.
6. **Adicionar Moedas** (`adicionar_moedas`): Testa a adição de moedas à conta do usuário, garantindo que o usuário exista e o valor seja corretamente atualizado.
7. **Busca de Valores** (`buscar_valores`): Verifica se a busca de valores específicos, como idade ou moedas, é realizada corretamente.
8. **Verificação de Índice de Usuário** (`verifica_usurio_index`): Retorna o índice do usuário na lista de dados cadastrados, levantando exceções caso o usuário não seja encontrado.

## 🧪 Como Executar os Testes

1. **Certifique-se de ter o Python 3.x instalado.**
2. **Clone este repositório:**
   ```bash
   git clone https://github.com/seu-repositorio.git
   ```
3. **Navegue até o diretório do projeto:**
   ```bash
   cd seu-repositorio
   ```
4. **Execute os testes com o seguinte comando:**
   ```bash
   python -m unittest discover tests/
   ```

Isso irá executar todos os testes unitários presentes no projeto.

## 💻 Exemplo de Uso

```python
from serviceUser import cadastro_usuario, login_usuario

# Cadastro de um novo usuário
cadastro_usuario('joao', 'senha123', 'Rua A', 'joao@gmail.com', 25)

# Login de um usuário
login_usuario('joao', 'senha123')
```

## 🤝 Contribuindo

Sinta-se à vontade para contribuir com este projeto. Crie um fork, implemente suas alterações e submeta um pull request!

1. Faça o fork do projeto.
2. Crie uma nova branch: `git checkout -b minha-branch`.
3. Commit suas mudanças: `git commit -m 'Adiciona nova funcionalidade'`.
4. Envie para o repositório remoto: `git push origin minha-branch`.
5. Abra um Pull Request.

