from classes.hunter_class import hunter
from classes.local_class import local
from classes.enemie_class import enemie
from data import items_data
import os
import random

def explore(personagem: hunter, lugar: local):
    os.system("cls")
    
    r = random.randint(0, 5)

    match r:
        #inimigo
        case 0:
            inimigos_possiveis = len(lugar.inimigos)-1
            inimigo_escolhido = lugar.inimigos[random.randint(0, inimigos_possiveis)]
            inimigo = enemie(inimigo_escolhido)

            fight(personagem, inimigo)

        #achar moedas 
        case 1:
            moedas_encontradas = random.randint(2, 10)
            personagem.qtd_moedas += moedas_encontradas
            print(f"Você encontrou {moedas_encontradas} moedas.")
            print(f"Agora você {personagem.qtd_moedas} moedas.")

        #achar nada
        case 5:
            print("Não encontrou nada.")

def show_atributes(personagem: hunter):
    os.system("cls")

    print(personagem.atributos)

def show_inventory(personagem: hunter):
    os.system("cls")

    print(personagem.inventario)
    print(f"Moedas: {personagem.qtd_moedas}")

def shop():
    print(items_data.pocao)

def fight(personagem: hunter, inimigo: enemie):
    print(personagem.nome, personagem.arma.nome, personagem.atributos["HP"])
    print(inimigo.nome, inimigo.moedas)