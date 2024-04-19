'''
Exercício 1 - Triângulo - Especifique um conjunto de casos de teste para testar o programa a seguir:

"O programa lê três valores inteiros que representam os lados de um triângulo. O programa informa se os lados formam um triângulo isósceles, escaleno ou equilátero."

Condição: a soma de dois lados tem que ser maior que o terceiro lado.

1. Defina o esqueleto de uma classe Java que resolva o problema acima.
2. Escreva casos de teste JUnit para as seguintes situações:
    1. Triângulo escaleno válido
    2. Triângulo isósceles válido
    3. Triângulo equilatero válido
    4. Pelo menos 3 casos de teste (CTs) para isósceles válido contendo a permutação dos mesmos valores
    5. Um valor zero
    6. Um valor negativo
    7. A soma de 2 lados é igual ao teceiro lado
    8. Para o item acima, um CT para cada permutação de valores
    9. CT em que a soma de 2 lados é menor que o terceiro lado
    10. Para o item acima, um CT para cada permutação de valores
    11. Um CT para os três valores iguais a zero
    
'''
import sys, os

# cur_path = os.path.dirname(os.path.abspath(__file__))
# head, tail = os.path.split(os.path.split(cur_path)[0])
# sys.path.insert(0, os.path.join(head, 'src'))
# sys.path.insert(1, os.path.join(head, 'tests'))

# Biblioteca unitest para realizar os testes
import unittest
from triangulo import Triangulo

#  ----- Função do Triangulo -----


# ------ Testes do Triangulo ------

class TestTriangulo(unittest.TestCase):
    def setUp(self):
        self.triangulo = Triangulo()
        
    def test_escaleno_valido(self):
        self.assertEqual("Triângulo Escaleno", self.triangulo.tipo_triangulo(3, 4, 5))
        
    def test_isosceles_valido(self):
        self.assertEqual("Triângulo Isósceles", self.triangulo.tipo_triangulo(5, 5, 3))
        
    def test_equilatero_valido(self):
        self.assertEqual("Triângulo Equilátero", self.triangulo.tipo_triangulo(2, 2, 2))
        
    def test_isosceles_valido_permutacao_1(self):
        self.assertEqual("Triângulo Isósceles", self.triangulo.tipo_triangulo(5, 3, 5))
        
    def test_isosceles_valido_permutacao_2(self):
        self.assertEqual("Triângulo Isósceles", self.triangulo.tipo_triangulo(3, 5, 5))
        
    def test_isosceles_valido_permutacao_3(self):
        self.assertEqual("Triângulo Isósceles", self.triangulo.tipo_triangulo(5, 5, 3))
        
    def test_valor_zero(self):
        self.assertEqual("Não é um triângulo válido", self.triangulo.tipo_triangulo(0, 2, 3))
        
    def test_valor_negativo(self):
        self.assertEqual("Não é um triângulo válido", self.triangulo.tipo_triangulo(-1, 2, 3))
        
    def test_soma_dois_lados_igual_terceiro_lado(self):
        self.assertEqual("Não é um triângulo válido", self.triangulo.tipo_triangulo(1, 2, 3))
        
    def test_soma_dois_lados_menor_terceiro_lado_permutacao_1(self):
        self.assertEqual("Não é um triângulo válido", self.triangulo.tipo_triangulo(1, 2, 6))
        
    def test_soma_dois_lados_menor_terceiro_lado_permutacao_2(self):
        self.assertEqual("Não é um triângulo válido", self.triangulo.tipo_triangulo(6, 1, 2))
        
    def test_soma_dois_lados_menor_terceiro_lado_permutacao_3(self):
        self.assertEqual("Não é um triângulo válido", self.triangulo.tipo_triangulo(2, 6, 1))
        
    def test_todos_os_lados_iguais_zero(self):
        self.assertEqual("Não é um triângulo válido", self.triangulo.tipo_triangulo(0, 0, 0))

