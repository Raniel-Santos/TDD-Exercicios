'''
Considera o conjunto de classes abaixo. Utilizando um abordagem TDD, implemente o método isValidToInclude(). Esse método deve retornar uma lista de erros com base no objeto Pessoa passado como parâmetro. Deve ser validado:
    - O nome é composto por ao menos 2 partes e deve ser composto de letras
    - A idade deve estar no intervalo [1, 200]
    - O objeto Person deve ter pelo menos um objeto da classe Email associado
    - O nome da classe Email deve estar no formato "_____@____._____", sendo que cada parte deve ter ao menos um caractere
'''

import unittest

from pessoa import PessoaDAO ,Pessoa , Email



# ------ Testes do Pessoa ------

class TestPessoa(unittest.TestCase):
    def setUp(self):
        self.dao = PessoaDAO()

    def test_nome_valido(self):
        self.dao = PessoaDAO()
        valid_nome = "Abel Ferreira"
        self.assertTrue(self.dao.nome_e_valido(valid_nome))

    def test_nome_invalido(self):
        invalid_nome1 = "Abel"
        invalid_nome2 = "123Palmeiras"
        invalid_nome3 = "Abel123Palmeiras"
        self.assertFalse(self.dao.nome_e_valido(invalid_nome1))
        self.assertFalse(self.dao.nome_e_valido(invalid_nome2))
        self.assertFalse(self.dao.nome_e_valido(invalid_nome3))

    def test_idade_valida(self):
        valid_idade = 30
        self.assertTrue(self.dao.idade_e_valida(valid_idade))

    def test_idade_invalida(self):
        invalid_idade1 = 0
        invalid_idade2 = 201
        self.assertFalse(self.dao.idade_e_valida(invalid_idade1))
        self.assertFalse(self.dao.idade_e_valida(invalid_idade2))

    def test_email_valido(self):
        self.dao = PessoaDAO()
        valid_email = "raniel.paula@fatec.sp.gov.br"
        self.assertTrue(self.dao.email_e_valido(valid_email))

    def test_email_invalido(self):
        self.dao = PessoaDAO()
        email_invalido = "raniel@raniel"
        self.assertFalse(self.dao.email_e_valido(email_invalido))
    
    def test_pessoa_com_email(self):
        pessoa_com_email = Pessoa(3, "Raniel Santos", 30)
        pessoa_com_email.emails.append(Email(2, "raniel.paula@fatec.sp.gov.br"))
        self.assertTrue(self.dao.pessoa_tem_email(pessoa_com_email.emails))

    def test_pessoa_sem_email(self):
        pessoa_sem_email = Pessoa(4, "Raniel Santos", 30)
        self.assertFalse(self.dao.pessoa_tem_email(pessoa_sem_email.emails))

    def test_salvar_pessoa(self):
        pessoa = Pessoa(1, "Raniel Santos", 30)
        pessoa.emails.append(Email(1, "raniel.paula@fatec.sp.gov.br"))
        self.dao.save(pessoa)
        self.assertEqual(len(self.dao.pessoas), 1)

    def test_salvar_pessoa_com_email_invalido(self):
        pessoa = Pessoa(2, "Raniel Santos", 30)
        pessoa.emails.append(Email(2, "raniel.paulafatec.sp.gov.br"))
        erros = self.dao.isValidToInclude(pessoa)
        self.assertEqual(erros, ["Email inválido, Formato correto é _____@____._____"])

    def test_salvar_pessoa_com_nome_invalido(self):
        pessoa = Pessoa(2, "Abel", 30)
        pessoa.emails.append(Email(2, "raniel.paula@fatec.sp.gov.br"))
        erros = self.dao.isValidToInclude(pessoa)
        self.assertEqual(erros, ['Nome inválido'])

    def test_salvar_pessoa_com_idade_invalida(self):
        pessoa = Pessoa(2, "Raniel Santos", 0)
        pessoa.emails.append(Email(2, "raniel.paula@fatec.sp.gov.br"))
        erros = self.dao.isValidToInclude(pessoa)
        self.assertEqual(erros, ["Idade inválida"])
    
    def test_salvar_pessoa_sem_email(self):
        pessoa = Pessoa(2, "Raniel Santos", 30)
        erros = self.dao.isValidToInclude(pessoa)
        self.assertEqual(erros, ["A Pessoa deve ter pelo menos um Email associado"])