from calculadora import CalculadoraCientifica
import unittest

class TesteCalculadora(unittest.TestCase):

    def setUp(self):
        self.calc = CalculadoraCientifica

    def teste_subtracao(self):
        self.assertEqual(self.calc.subtracao(7014235,198462),6815773)
        self.assertNotEqual(self.calc.subtracao(10,5),)

if __name__ == '__main__':
    unittest.main()