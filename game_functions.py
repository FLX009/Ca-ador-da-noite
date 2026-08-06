import json
import os
import random
from pathlib import Path

from classes.enemy_class import Enemy
from classes.hunter_class import Hunter
from classes.item_class import Item
from classes.local_class import Local
from classes.weapon_class import Weapon
from combat import fight
from data import items_data
from data.items_data import converte_efeito_json
from utils import add_item, esperar, print_item


def explore(personagem: Hunter, lugar: Local):
    r = random.randint(0, 4)

    match r:
        # inimigo
        case 0:
            inimigos_possiveis = len(lugar.inimigos) - 1
            inimigo_escolhido = lugar.inimigos[random.randint(0, inimigos_possiveis)]
            inimigo = Enemy(inimigo_escolhido.copy())

            fight(personagem, inimigo)

        # achar moedas
        case 1:
            moedas_encontradas = random.randint(2, 10)
            personagem.qtd_moedas += moedas_encontradas
            print(f"Você encontrou {moedas_encontradas} moedas.")
            print(f"Agora você {personagem.qtd_moedas} moedas.")

        # item
        case 2:
            item_achado = items_data.pocao
            add_item(item_achado, personagem)
            print("achou poção")

        # armadilha
        case 3:
            personagem.hp -= 2
            print("Você caiu em uma armadilha")
            print("Tomou 2 de dano")
            print(f"HP: {personagem.hp}/{personagem.atributos['max HP']}")
            esperar()

        # achar nada
        case 4:
            print("Não encontrou nada.")


def show_atributes(personagem: Hunter):
    """Mostrar os atributos."""
    print(f"HP: {personagem.hp}/{personagem.atributos["max HP"]}")
    for k, v in personagem.atributos.items():
        if k != "max HP":
            print(f"{k} : {v}")


def show_inventory(personagem: Hunter):
    """Mostrar inventario."""
    for i in personagem.inventario:
        print(f"{i.nome} x{i.quantidade}")

    print(f"Moedas: {personagem.qtd_moedas}")


def shop(personagem):
    """Abrir loja."""
    print_item(items_data.pocao)
    print()
    print(f"Moedas: {personagem.qtd_moedas}")


def save(personagem, lugar):
    with open("save.json", "w") as save:
        json.dump(
            (
                personagem.to_dict(),
                personagem.arma.to_dict(),
                lugar.to_dict(),
            ),
            save,
            indent=2,
        )


def load_save():
    with open("save.json", "r") as save:
        data = json.load(save)
        personagem_data = data[0]
        arma_data = data[1]
        lugar_data = data[2]

    # Converter a string [efeito] para função de efeito.
    for i in personagem_data["inventario"]:
        for k, v in converte_efeito_json.items():
            if i["efeito"] == k:
                i["efeito"] = v
                break

    # Criar os objetos a partir do save.
    personagem = Hunter(
        personagem_data["nome"],
        personagem_data["idade"],
        personagem_data["hp"],
        personagem_data["origem"],
        Weapon(arma_data),
        personagem_data["qtd_moedas"],
        personagem_data["atributos"],
    )

    for i in personagem_data["inventario"]:
        item_json = Item(i, i["quantidade"])
        personagem.inventario.append(item_json)

    lugar = Local(lugar_data)

    return personagem, lugar


def delete_save():
    if Path("save.json").exists():
        os.remove("save.json")
        print("Deletado")
        esperar()
        return True
    else:
        print("Não existe um save")
        esperar()
        return False
