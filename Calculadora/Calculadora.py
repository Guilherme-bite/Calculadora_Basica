def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro: divisão por zero"

def porcentagem(a, b):
    return (a * b) / 100

def potenciacao(a, b):
    return a ** b

def menu():
    print("==== Calculadora Básica ====")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Porcentagem")
    print("6 - Potenciação")
    print("0 - Sair")

while True:
    menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "0":
        print("Encerrando calculadora...")
        break

    if opcao in ["1", "2", "3", "4", "5", "6"]:
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
        except ValueError:
            print("Entrada inválida! Digite apenas números.")
            continue

        if opcao == "1":
            print("Resultado:", soma(num1, num2))
        elif opcao == "2":
            print("Resultado:", subtracao(num1, num2))
        elif opcao == "3":
            print("Resultado:", multiplicacao(num1, num2))
        elif opcao == "4":
            print("Resultado:", divisao(num1, num2))
        elif opcao == "5":
            print(f"{num2}% de {num1} é:", porcentagem(num1, num2))
        elif opcao == "6":
            print(f"{num1} elevado a {num2} é:", potenciacao(num1, num2))
    else:
        print("Opção inválida! Escolha de 0 a 6.")
