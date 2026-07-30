import time
import os
from classes.item_class import Item

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

def print_item(Item):
    for k, v in Item.items():
        if k not in ("efeito", "qtd_efeito"):
            print(f"{k}: {v}")

def add_item(item_add, Personagem, quantos = 1):
    for i in Personagem.inventario:
        if i.nome == item_add["nome"]:
           i.quantidade += quantos
           return

    novo_item = Item(item_add, quantos)
    Personagem.inventario.append(novo_item)