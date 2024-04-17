import math

class CalculadoraCientifica:
    def __init__(self):
        self.ultimo_resultado = None
    
    def adicao(self, n1:int, n2:int):
        self.ultimo_resultado = n1 + n2
        return self.ultimo_resultado
    
    def subtracao(self, n1:int, n2:int):
        self.ultimo_resultado = n1 - n2
        return self.ultimo_resultado
    
    def multiplicacao(self, n1:int, n2:int):
        self.ultimo_resultado = n1 * n2
        return self.ultimo_resultado
    
    def divisao(self, n1:int, n2:int):
        if n2 == 0 or n1 == 0:
            raise ZeroDivisionError('Divisão Por Zero')
        self.ultimo_resultado = n1 / n2
        return self.ultimo_resultado
    
    def potenciacao(self, base:int, expoente:int):
        self.ultimo_resultado = base ** expoente
        return self.ultimo_resultado

    def raiz_quadrada(self, n1:int):
        if n1 < 0:
           raise ValueError('Número negativo inserido')
        self.ultimo_resultado = math.sqrt(n1)
        return self.ultimo_resultado
    
    def logaritmo(self, log, base):
        return math.log(log,base)
    
    def seno(self,angulo):
        radianos = math.radians(angulo)
        self.ultimo_resultado = f"{math.sin(radianos):.2f}"
        return self.ultimo_resultado
    
    def cosseno(self,angulo):
        radianos = math.radians(angulo)
        self.ultimo_resultado =f"{math.cos(radianos):.2f}"
        return self.ultimo_resultado

    def tangente(self,angulo):
        radianos = math.radians(angulo)
        self.ultimo_resultado = f"{math.tan(radianos):.2f}"
        return self.ultimo_resultado