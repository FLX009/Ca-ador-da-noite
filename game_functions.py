from classes.hunter_class import Hunter
from classes.local_class import Local
from classes.enemy_class import Enemy
from classes.item_class import Item
from utils import print_item, add_item, esperar
from combat import fight
from data import items_data
import random

def explore(personagem: Hunter, lugar: Local):
    r = random.randint(0, 4)

    match r:
        #inimigo
        case 0:
            inimigos_possiveis = len(lugar.inimigos)-1
            inimigo_escolhido = lugar.inimigos[random.randint(0, inimigos_possiveis)]
            inimigo = Enemy(inimigo_escolhido.copy())

            fight(personagem, inimigo)

        #achar moedas 
        case 1:
            moedas_encontradas = random.randint(2, 10)
            personagem.qtd_moedas += moedas_encontradas
            print(f"Você encontrou {moedas_encontradas} moedas.")
            print(f"Agora você {personagem.qtd_moedas} moedas.")

        #item
        case 2:
            item_achado = items_data.pocao
            add_item(item_achado, personagem)
            print("achou poção")

        #armadilha
        case 3:
            personagem.hp -= 2
            print("Você caiu em uma armadilha")
            print("Tomou 2 de dano")
            esperar()

        #achar nada
        case 4:
            print("Não encontrou nada.")

def show_atributes(personagem: Hunter):
    for k, v in personagem.atributos.items():
        print(f"{k} : {v}")

def show_inventory(personagem: Hunter):
    for i in personagem.inventario:
        print(f"{i.nome} x{i.quantidade}")

    print(f"Moedas: {personagem.qtd_moedas}")

def use_item(personagem):
    itens_inventario = set()
    for i in personagem.inventario:
        print(f"{i.nome} x{i.quantidade}")
        itens_inventario.add(i.nome)

    resposta = input("Escreva o nome do item para usar: ")

    if resposta in itens_inventario:
        for i in personagem.inventario:
            if i.nome == resposta:
                i.efeito(personagem, i.qtd_efeito)
                if i.quantidade == 1:
                    personagem.inventario.remove(i)
                else:
                    i.quantidade -= 1
                print("Item usado.")
                esperar()
                break
    else:
        print("Item não encontrado")
        esperar()

def shop(personagem):
    print_item(items_data.pocao)
    print("")
    print(f"Moedas: {personagem.qtd_moedas}")