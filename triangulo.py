class Triangulo:    
    def tipo_triangulo(self, lado1, lado2, lado3):
        if lado1 <= 0 or lado2 <= 0 or lado3 <= 0:
            return "Não é um triângulo válido"
        
        if lado1 + lado2 <= lado3 or lado1 + lado3 <= lado2 or lado2 + lado3 <= lado1:
            return "Não é um triângulo válido"
        
        if lado1 == lado2 == lado3:
            return "Triângulo Equilátero"
        elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
            return "Triângulo Isósceles"
        else:
            return "Triângulo Escaleno"