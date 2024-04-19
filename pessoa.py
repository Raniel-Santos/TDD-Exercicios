# ----- Funções do Person -----
import re
from typing import List
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