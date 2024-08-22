from Calculadora import Calculadora


def main():
    # Solicitando entrada do usuário
    try:
        valorA = float(input("Digite o valor A: "))
        valorB = float(input("Digite o valor B: "))
        operacao = input("Digite a operação (+, -, *, /): ")
    except ValueError:
        print("Entrada inválida. Certifique-se de digitar números válidos.")
        return

    # Criando uma nova instância da Calculadora
    calc = Calculadora(valorA, valorB, operacao)

    # Exibindo o resultado
    calc.mostrarResultado()


if __name__ == "__main__":
    main()