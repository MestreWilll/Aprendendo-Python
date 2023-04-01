def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Erro: divisão por zero.")
        return None

def calculadora():
    print("Selecione a operação:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")

    escolha = input("Digite sua escolha (1/2/3/4): ")

    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if escolha == '1':
        print("Resultado:", soma(num1, num2))
    elif escolha == '2':
        print("Resultado:", subtracao(num1, num2))
    elif escolha == '3':
        print("Resultado:", multiplicacao(num1, num2))
    elif escolha == '4':
        resultado = divisao(num1, num2)
        if resultado is not None:
            print("Resultado:", resultado)
    else:
        print("Entrada inválida")

if __name__ == "__main__":
    calculadora()