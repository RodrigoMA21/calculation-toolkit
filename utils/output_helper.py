from colorama import Fore, Style

def sucesso(msg: str):
    print(Fore.GREEN + msg + Style.RESET_ALL)

def erro(msg: str):
    print(Fore.RED + msg + Style.RESET_ALL)