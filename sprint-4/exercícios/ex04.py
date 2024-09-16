def calcular_valor_maximo(operadores,operandos) -> float:
    def aplicar_operacao(op, x, y):
        if op == '+':
            return x + y
        elif op == '-':
            return x - y
        elif op == '*':
            return x * y
        elif op == '/':
            return x / y
        elif op == '%':
            return x % y

    operacoes = zip(operadores, operandos)
    resultados = map(lambda op_opds: aplicar_operacao(op_opds[0], *op_opds[1]), operacoes)
    return max(resultados)
