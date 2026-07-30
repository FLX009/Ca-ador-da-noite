import time
import os

def esperar():
    time.sleep(2)

def limpar():
    os.system("cls")

def pedir_inteiro(prompt = "", validador = None):
    while True:
        try:
            resposta = int(input(prompt))
            if validador is None or resposta in validador:
                break
            else:
                print("Inválido")
        except ValueError:
            print("Inválido")
    return resposta