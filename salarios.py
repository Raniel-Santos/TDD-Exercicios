class Funcionario:
    def __init__(self, nome, email, cargo, salario_base):
        self.nome = nome
        self.email = email
        self.cargo = cargo
        self.salario_base = salario_base
    
    def calcular_desconto_salario(self):
        if self.cargo == 'DESENVOLVEDOR':
            if self.salario_base >= 3000:
                return self.salario_base * 0.8
            else:
                return self.salario_base * 0.9
        elif self.cargo == 'DBA':
            if self.salario_base >= 2000:
                return self.salario_base * 0.75
            else:
                return self.salario_base * 0.85
        elif self.cargo == 'TESTADOR':
            if self.salario_base >= 2000:
                return self.salario_base * 0.75
            else:
                return self.salario_base * 0.85
        elif self.cargo == 'GERENTE':
            if self.salario_base >= 5000:
                return self.salario_base * 0.7
            else:
                return self.salario_base * 0.8
