from services.temperatura import celsius_para_fahrenheit
from services.fatorial import calcular_fatorial
from utils.input_helper import ler_float, ler_int
from utils.output_helper import sucesso, erro

from colorama import Fore, Style, init

init()


def mostrar_menu():
    print(Fore.CYAN + "\n=== Calculation Toolkit ===" + Style.RESET_ALL)
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
            sucesso(f"Resultado: {fahrenheit:.2f} °F")

        elif opcao == "2":
            numero = ler_int("Digite um número inteiro (0 ou positivo): ")

            if numero < 0:
                erro("Fatorial não existe para números negativos.")
                continue

            resultado = calcular_fatorial(numero)
            sucesso(f"Resultado: {numero}! = {resultado}")

        elif opcao == "0":
            print(Fore.YELLOW + "Encerrando o programa..." + Style.RESET_ALL)
            break

        else:
            erro("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    executar()