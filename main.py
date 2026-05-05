from services.temperatura import celsius_para_fahrenheit
from services.fatorial import calcular_fatorial
from utils.input_helper import ler_float, ler_int


def mostrar_menu():
    print("\n=== Calculation Toolkit ===")
    print("1 - Converter Celsius para Fahrenheit")
    print("2 - Calcular Fatorial")
    print("0 - Sair")


def executar():
    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            celsius = ler_float("Digite a temperatura em Celsius: ")
            fahrenheit = celsius_para_fahrenheit(celsius)
            print(f"Resultado: {fahrenheit:.2f} °F")

        elif opcao == "2":
            numero = ler_int("Digite um número inteiro (0 ou positivo): ")

            if numero < 0:
                print("Fatorial não existe para números negativos.")
                continue

            resultado = calcular_fatorial(numero)
            print(f"Resultado: {numero}! = {resultado}")

        elif opcao == "0":
            print("Encerrando o programa...")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    executar()