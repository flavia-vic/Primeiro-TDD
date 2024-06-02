import unittest
from calculator import calculator

# Classe de testes para a calculadora
class TestCalculator(unittest.TestCase):

    # Teste para verificar operação nula
    def test_operation_none(self):
        with self.assertRaises(Exception) as ex:
            calculator(None, 2, 2)
        self.assertEqual(ex.exception.args[0], 'Operação não pode ser nula')

    # Teste para verificar números inválidos
    def test_invalid_numbers(self):
        with self.assertRaises(Exception) as ex:
            calculator('add', None, 2)
        self.assertEqual(ex.exception.args[0], 'Informe dois números válidos para realizar a operação')
        
        with self.assertRaises(Exception) as ex2:
            calculator('add', 2, None)
        self.assertEqual(ex2.exception.args[0], 'Informe dois números válidos para realizar a operação')

    # Teste para verificar operação inválida
    def test_operation_valid(self):
        with self.assertRaises(Exception) as ex:
            calculator('fatorial', 10, 2)
        self.assertEqual(ex.exception.args[0], 'Informe uma operação válida (add, sub, mult, div)')

    # Teste para verificar soma
    def test_sum(self):
        result = calculator('add', 10, 30)
        self.assertEqual(result, 40)

    # Teste para verificar subtração
    def test_sub(self):
        result = calculator('sub', 50, 25)
        self.assertEqual(result, 25)

    # Teste para verificar multiplicação
    def test_mult(self):
        result = calculator('mult', 2, 5)
        self.assertEqual(result, 10)

    # Teste para verificar divisão
    def test_div(self):
        result = calculator('div', 10, 5)
        self.assertEqual(result, 2)

    # Teste para verificar divisão por zero
    def test_zero(self):
        with self.assertRaises(ZeroDivisionError) as z:
            calculator('div', 10, 0)
        self.assertEqual(z.exception.args[0], 'Você não pode dividir um número por 0')

if __name__ == '__main__':
    unittest.main()
