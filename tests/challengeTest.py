import unittest

from service.serviceUser import forca_opcao, senha_len, verifica_idade, cadastro_usuario, login_usuario, \
    dados_cadastrados, verifica_email_cadastro, email_existe, verifica_numero


class TestChallengeMethods(unittest.TestCase):

    # Testes da função verifica_email_cadastro
    def test_verifica_email_cadastro_deve_retormar_falso_caso_regex_nao_coincide_ja_existe(self):

        # já existe
        self.assertTrue(verifica_email_cadastro('edu@gm.com'))
        # probelmas com regex
        self.assertFalse(verifica_email_cadastro('qualquercoisa.com.br'))
        self.assertFalse(verifica_email_cadastro('eitanoisquecoisa'))
        self.assertFalse(verifica_email_cadastro('teste12'))

    # Testes da função login_usuario
    def test_login_usuario_retorna_falso_caso_usuario_nao_foi_cadastrado(self):

        self.assertFalse(login_usuario('teste12', 'senha1223'))
        self.assertFalse(login_usuario('qualquercoisa', 'senha12'))
        self.assertFalse(login_usuario('terceiro', 'tddebom'))

    # Testes da função verifica_idade
    def test_verifica_idade_deve_retornar_false_caso_for_de_menor_ou_se_nao_for_numero_retorna_3(self):

        # Verificando idade
        self.assertFalse(verifica_idade('3'))
        self.assertFalse(verifica_idade('12'))
        self.assertFalse(verifica_idade('17'))

        # Verificando se não for número
        self.assertEqual(verifica_idade('qualquercoisa'), 3)
        self.assertEqual(verifica_idade("['dsf']"), 3)
        self.assertEqual(verifica_idade('[123]'), 3)

    # Testes da função email_existe
    def test_email_existe_deve_retornar_false_se_nao_encontrar_email(self):
        dados_cadastrados = [
            {'id': 1, 'nome': 'edu', 'senha': 'edu', 'endereco': 'educ4', 'email': 'eduardodallabella@gmail.com', 'idade': 18, 'moedas': 100}]

        self.assertFalse(email_existe('luana@gmail.com.org', dados_cadastrados))
        self.assertFalse(email_existe('eduardo@gmail.com', dados_cadastrados))
        self.assertFalse(email_existe('luana@yahoo.com.br', dados_cadastrados))

    def test_email_existe_deve_retornar_o_email_do_usuario(self):
        dados_cadastrados = [
            {'id': 1, 'nome': 'edu', 'senha': 'edu', 'endereco': 'educ4', 'email': 'eduardodallabella@gmail.com',
             'idade': 18, 'moedas': 100},
            {'id': 1, 'nome': 'edu', 'senha': 'edu', 'endereco': 'educ4', 'email': 'robinson@gmail.com',
             'idade': 18, 'moedas': 100},
            {'id': 1, 'nome': 'edu', 'senha': 'edu', 'endereco': 'educ4', 'email': 'luana@gmail.com',
             'idade': 18, 'moedas': 100}
        ]

        self.assertEquals(email_existe('eduardodallabella@gmail.com', dados_cadastrados),'eduardodallabella@gmail.com' )
        self.assertEquals(email_existe('robinson@gmail.com', dados_cadastrados),'robinson@gmail.com' )
        self.assertEquals(email_existe('luana@gmail.com', dados_cadastrados),'luana@gmail.com' )


    # Testes da fução verifica_numero
    def test_verifica_numero_deve_retornar_falso_caso_nao_for_numero(self):

        self.assertFalse(verifica_numero('nao é numero'))
        self.assertFalse(verifica_numero('[12]'))
        self.assertFalse(verifica_numero('Opa!'))

    def test_verifica_numero_deve_retornar_true_caso_for_numero(self):

        self.assertTrue(verifica_numero('1'))
        self.assertTrue(verifica_numero(12))
        self.assertTrue(verifica_numero(2000))

    # Testes da função adicionar_moedas
    def test_adicionar_moedas_deve_cair_no_exepition_caso_nao_achar_usuario(self):
        dados_cadastrados = [
            {'id': 1, 'nome': 'edu', 'senha': 'edu', 'endereco': 'educ4', 'email': 'eduardodallabella@gmail.com',
             'idade': 18, 'moedas': 100},
            {'id': 1, 'nome': 'edu', 'senha': 'edu', 'endereco': 'educ4', 'email': 'robinson@gmail.com',
             'idade': 18, 'moedas': 100},
            {'id': 1, 'nome': 'edu', 'senha': 'edu', 'endereco': 'educ4', 'email': 'luana@gmail.com',
             'idade': 18, 'moedas': 100}
        ]
        self.assertFalse(False)


    def test_adicionar_moedas_deve_retornar_a_qnt_de_moedas_do_usuario(self):
        dados_cadastrados = [
            {'id': 1, 'nome': 'edu', 'senha': 'edu', 'endereco': 'educ4', 'email': 'eduardodallabella@gmail.com',
             'idade': 18, 'moedas': 100},
            {'id': 1, 'nome': 'edu', 'senha': 'edu', 'endereco': 'educ4', 'email': 'robinson@gmail.com',
             'idade': 18, 'moedas': 100},
            {'id': 1, 'nome': 'edu', 'senha': 'edu', 'endereco': 'educ4', 'email': 'luana@gmail.com',
             'idade': 18, 'moedas': 100}
        ]
        self.assertFalse(False)



    # Testes da função buscar_valores
    def test_buscar_valores_deve_cair_no_exeption_caso_nao_encontra_valor_do_usuario(self):
        self.assertFalse(False)
    def test_buscar_valores_retorna_index_do_valor_do_usuario_caso_encontra_usuario(self):
        self.assertFalse(False)


    # Testes da função verifica_usurio_index
    def test_verifica_usurio_index_deve_cair_no_exeption_caso_nao_encontrar_usuario(self):
        self.assertFalse(False)

    def test_verifica_usurio_index_deve_retornar_index_do_usario_caso_encontrar_usuario(self):
        self.assertFalse(False)

