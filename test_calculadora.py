#importando o pacote de testes unitarios

import unittest

#importando a classe 'Calculadora' pelo arquivo 'Calculadora.py'

from calculadora import Calculadora

#criando as classes de testes unitarios chamada 'TestCalculadora'
class TestCalculadora(unittest.TestCase):
    
    # Criando o metodo de definição do objeto que herdará a classe 'Calculadora' chamdo 'setUp'

    def setUp(self):
        self.calc= Calculadora()

    # Criando o teste  do método 'soma' da classe 'Calculadora'
    def test_soma(self):
        self.assertEqual(self.calc.soma(10, 20), 30)


         # Criando o teste  do método 'subtração' da classe 'Calculadora'
    def test_sub(self):
        self.assertEqual(self.calc.sub(10, 20), -10)

         # Criando o teste  do método 'Multiplicação' da classe 'Calculadora'
    def test_mult(self):
        self.assertEqual(self.calc.mult(10, 20), 200)

         # Criando o teste  do método 'Divisão' da classe 'Calculadora'
    def test_div(self):
        self.assertEqual(self.calc.div(10, 20), 0.5)

# Chamando a classe de Testes Unitários

if __name__ == '__main__':
    unittest.main()
