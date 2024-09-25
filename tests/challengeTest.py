import unittest

from service.serviceUser import forca_opcao, senha_len, verifica_idade, cadastro_usuario, login_usuario, \
    dados_cadastrados, verifica_email_cadastro


class TestChallengeMethods(unittest.TestCase):

    def test_verifica_email_cadastro_deve_retormar_falso_caso_regex_nao_coincide_ja_existe(self):

        # já existe
        self.assertFalse(verifica_email_cadastro('edu@gm.com'))
        # probelmas com regex
        self.assertFalse(verifica_email_cadastro('qualquercoisa.com.br'))
        self.assertFalse(verifica_email_cadastro('eitanoisquecoisa'))
        self.assertFalse(verifica_email_cadastro('teste12'))

    def test_login_usuario_retorna_falso_caso_usuario_nao_foi_cadastrado(self):

        self.assertFalse(login_usuario('teste12', 'senha1223'))
        self.assertFalse(login_usuario('qualquercoisa', 'senha12'))
        self.assertFalse(login_usuario('terceiro', 'tddebom'))

    def test_verifica_idade_deve_retornar_false_caso_for_de_menor_ou_se_nao_for_numero_retorna_3(self):

        # Verificando idade
        self.assertFalse(verifica_idade('3'))
        self.assertFalse(verifica_idade('12'))
        self.assertFalse(verifica_idade('17'))

        # Verificando se não for número
        self.assertEqual(verifica_idade('qualquercoisa'), 3)
        self.assertEqual(verifica_idade("['dsf']"), 3)
        self.assertEqual(verifica_idade('[123]'), 3)

    def test_verifica_o_usuario_e_retorna_qualquer_valor_respectivo_do_usuario(self):

        self.assertEqual('aabba', 'aabba')

    def test_busca_o_dado_do_usuario(self):

        self.assertTrue()

