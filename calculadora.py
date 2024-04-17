import math

class CalculadoraCientifica:
    def __init__(self):
        self.ultimo_resultado = None
    
    def adicao(self, n1:int, n2:int):
        self.ultimo_resultado = n1 + n2
        return self.ultimo_resultado
    
    def subtracao(self, n1:int, n2:int):
        return n1 - n2
    
    def multiplicacao(self, n1:int, n2:int):
        return n1 * n2
    
    def divisao(self, n1:int, n2:int):
        if n2 == 0 or n1 == 0:
            raise ZeroDivisionError('Divisão Por Zero')
        return n1 / n2
    
    def potenciacao(self, base:int, expoente:int):
        return base ** expoente

    def raiz_quadrada(self, n1:int):
        if n1 < 0:
           raise ValueError('Número negativo inserido')
        return math.sqrt(n1)
    
    def logaritmo(self, log, base):
        return math.log(log,base)
    
    def seno(self,angulo):
        radianos = math.radians(angulo)
        return f"{math.sin(radianos):.2f}"
    
    def cosseno(self,angulo):
        radianos = math.radians(angulo)
        return f"{math.cos(radianos):.2f}"

    def tangente(self,angulo):
        radianos = math.radians(angulo)
        return f"{math.tan(radianos):.2f}"