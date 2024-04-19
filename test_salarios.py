'''
Seguindo um ciclo de Test Driven Development (TDD), desenvolva as classes necessárias para resolver o problema descrito abaixo:

    O participante deve implementar uma calculadora de salário de funcionários. Um funcionário contem nome, email, salário-base e cargo. De acordo com seu cargo, a regra para cálculo do salário líquido é diferente:
        - Caso o cargo seja DESENVOLVEDOR, o funcionário terá desconto de 20% caso o salário seja maior ou igual que 3.000,00, ou apenas 10% caso o salário seja menor que isso;
        - Caso o cargo seja DBA, o funcionário terá desconto de 25% caso o salário seja maior ou igual que 2.000,00, ou apenas 15% caso o salário seja menor que isso;
        - Caso o cargo seja TESTADOR, o funcionário terá desconto de 25% caso o salário seja maior ou igual que 2.000,00, ou apenas 15% caso o salário seja menor que isso; e
        - Caso o cargo seja GERENTE, o funcionário terá desconto de 30% caso o salário seja maior ou igual que 5.000,00, ou apenas 20% caso o salário seja menor que isso.
    '''

import unittest
# ----- Funções do Salario -----
from salarios import Funcionario



# ----- Testes do Salario -----
class TestSalarioFuncionario(unittest.TestCase):      

    def test_salario_de_desenvolvedor_maior_ou_igual_3k_desc_20_por_cento(self):
        funcionario = Funcionario('Rafael', 'rafael@email.com', 'DESENVOLVEDOR', 3650)
        self.assertEqual(funcionario.calcular_desconto_salario(), 2920)

    def test_salario_de_desenvolvedor_menor_3k_desc_10_por_cento(self):
        funcionario = Funcionario("Maria", "maria@email.com", "DESENVOLVEDOR", 2600)
        self.assertEqual(funcionario.calcular_desconto_salario(), 2340)

    def test_salario_de_dba_maior_ou_igual_2k_desc_25_por_cento(self):
        funcionario = Funcionario("Pedro", "pedro@email.com", "DBA", 4000)
        self.assertEqual(funcionario.calcular_desconto_salario(), 3000)

    def test_salario_de_dba_menor_2k_desc_15_por_cento(self):
        funcionario = Funcionario("Ana", "ana@email.com", "DBA", 1900)
        self.assertEqual(funcionario.calcular_desconto_salario(), 1615)

    def test_salario_de_testador_maior_ou_igual_2k_desc_25_por_cento(self):
        funcionario = Funcionario("Raniel", "raniel@email.com", "TESTADOR", 4000)
        self.assertEqual(funcionario.calcular_desconto_salario(), 3000)

    def test_salario_de_testador_menor_2k_desc_15_por_cento(self):
        funcionario = Funcionario("Aline", "aline@email.com", "TESTADOR", 1900)
        self.assertEqual(funcionario.calcular_desconto_salario(), 1615)

    def test_salario_de_gerente_maior_ou_igual_5k_desc_30_por_cento(self):
        funcionario = Funcionario("Abel", "abel@email.com", "GERENTE", 6000)
        self.assertEqual(funcionario.calcular_desconto_salario(), 4200)

    def test_salario_de_gerente_menor_5k_desc_20_por_cento(self):
        funcionario = Funcionario("Luana", "luana@email.com", "GERENTE", 4000)
        self.assertEqual(funcionario.calcular_desconto_salario(), 3200)

    
