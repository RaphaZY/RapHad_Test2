from calculadora import CalculadoraCientifica
import unittest

class TesteCalculadora(unittest.TestCase):
    
    def setUp(self):
        self.calc = CalculadoraCientifica()

    def test_adicao(self):
        self.assertEqual(self.calc.adicao(150,150),300)
        self.assertEqual(self.calc.adicao(123,432),555)
        self.assertNotEqual(self.calc.adicao(4,2),7)
        self.assertNotEqual(self.calc.adicao(20,10),31)
        self.assertIsNotNone(self.calc.adicao(20,30))
    
    def test_subtracao(self):
        self.assertEqual(self.calc.subtracao(2,2),0)
        self.assertEqual(self.calc.subtracao(10,5),5)
        self.assertEqual(self.calc.subtracao(11,12),-1)
        self.assertEqual
        
if __name__ == '__main__':
    unittest.main()