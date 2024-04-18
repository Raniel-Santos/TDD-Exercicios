'''
Considera o conjunto de classes abaixo. Utilizando um abordagem TDD, implemente o método isValidToInclude(). Esse método deve retornar uma lista de erros com base no objeto Pessoa passado como parâmetro. Deve ser validado:
    - O nome é composto por ao menos 2 partes e deve ser composto de letras
    - A idade deve estar no intervalo [1, 200]
    - O objeto Person deve ter pelo menos um objeto da classe Email associado
    - O nome da classe Email deve estar no formato "_____@____._____", sendo que cada parte deve ter ao menos um caractere
'''
import re
from typing import List
import unittest


# ----- Funções do Person -----
class Pessoa:
    def __init__(self, id: int,  nome: str, idade):
        self.id = id
        self.nome = nome
        self.idade = idade
        self.emails = []

class Email:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome

class PessoaDAO:
    def __init__(self):
        self.pessoas = []

    def save(self, pessoa):
        erros = self.isValidToInclude(pessoa)
        if len(erros) == 0:
            self.pessoas.append(pessoa)

    def isValidToInclude(self, pessoa):
        erros = []
        if not self.nome_e_valido(pessoa.nome):
            erros.append("Nome inválido")
        if not self.idade_e_valida(pessoa.idade):
            erros.append("Idade inválida")
        if not self.pessoa_tem_email(pessoa.emails):
            erros.append("A Pessoa deve ter pelo menos um Email associado") 
        for email in pessoa.emails:
            if not self.email_e_valido(email.nome):
                erros.append("Email inválido, Formato correto é _____@____._____")
            print(erros)
        return erros
    
    def nome_e_valido(self, nome: str) -> bool:
        nomes = nome.split(" ")
        tem_digito = bool(re.search(r"\d", nome))
        if len (nomes) >= 2 and not tem_digito:
            return True
        return False
    
    def idade_e_valida(self, idade:int):
        if idade in range(1,201):
            return True
        return False

    def pessoa_tem_email(self, emails: List[Email]):
        if len(emails) >= 1:
            return True
        else:
            return False
    
    def email_e_valido(self, email):
        padrao_email = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        return re.match(padrao_email, email)is not None
    

# ------ Testes do Pessoa ------

class TestPessoa(unittest.TestCase):
    def setUp(self):
        self.dao = PessoaDAO()

    def test_nome_valido(self):
        # Teste para nome válido
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


if __name__ == '__main__':
    unittest.main()