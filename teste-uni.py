from calculadora import CalculadoraCientifica
import unittest

class TesteCalculadora(unittest.TestCase):

    def setUp(self):
        self.calc = CalculadoraCientifica()

    def test_filtrar(self):
        pass

    def test_adicao(self):
        self.assertEqual(self.calc.adicao(150,150),300)
        self.assertEqual(self.calc.adicao(123,432),555)
        self.assertNotEqual(self.calc.adicao(4,2),7)
        self.assertNotEqual(self.calc.adicao(20,10),31)
        self.assertEqual(self.calc.adicao(-1,-1),-2)
        self.assertIsNotNone(self.calc.adicao(20,30))
        #with self.assertRises(TypeError):
            #self.calc.adicao('a','b')

    def test_subtracao(self):
        self.assertEqual(self.calc.subtracao(2,2),0)
        self.assertEqual(self.calc.subtracao(10,5),5)
        self.assertEqual(self.calc.subtracao(11,12),-1)
        self.assertNotEqual(self.calc.subtracao(50,40),11)
        self.assertIsNotNone(self.calc.subtracao(20,30))
        
    def test_divisao(self):
        with self.assertRaises(ZeroDivisionError):
            self.calc.divisao(1,0)
        self.assertEqual(self.calc.divisao(10000,10),1000)
        self.assertEqual(self.calc.divisao(16,4),4)
    
    def test_raiz_quadrada(self):
        self.assertEqual(self.calc.raiz_quadrada(25),5)
        with self.assertRaises(ValueError):
            self.calc.raiz_quadrada(-25)
        self.assertNotEqual(self.calc.raiz_quadrada(100),1)
    
    def test_logaritimo(self):
        self.assertEqual(self.calc.logaritmo(10,10),1)
        self.assertNotEqual(self.calc.logaritmo(20,10),1)
        
    def test_potenciacao(self):
        self.assertEqual(self.calc.potenciacao(5,2),25)
        self.assertEqual(self.calc.potenciacao(10,3),1000)

   
    
        



if __name__ == '__main__':
    unittest.main()