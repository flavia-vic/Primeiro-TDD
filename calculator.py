# Função principal da calculadora, realiza operações básicas com validação de parâmetros
def calculator(operation, num1, num2):
    # Valida os parâmetros de entrada
    validate(operation, num1, num2)
    
    # Executa a operação de acordo com o tipo especificado
    if operation == 'add':
        return num1 + num2
    elif operation == 'sub':
        return num1 - num2
    elif operation == 'mult':
        return num1 * num2
    elif operation == 'div':
        try:
            return num1 / num2
        except ZeroDivisionError:
            raise ZeroDivisionError('Você não pode dividir um número por 0')

# Função de validação dos parâmetros de entrada
def validate(operation, num1, num2):
    # Verifica se a operação é nula
    if operation is None:
        raise Exception('Operação não pode ser nula')
    # Verifica se algum dos números é nulo
    if num1 is None or num2 is None:
        raise Exception('Informe dois números válidos para realizar a operação')
    # Verifica se a operação é válida
    if operation not in ['add', 'sub', 'mult', 'div']:
        raise Exception('Informe uma operação válida (add, sub, mult, div)')
