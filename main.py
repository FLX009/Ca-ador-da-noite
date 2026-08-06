import json
from pathlib import Path

from assets.ascii import (
    criar_personagem_ascii,
    derrota_ascii,
    fim_de_jogo_ascii,
    menu_ascii,
    titulo_ascii,
)
from assets.text import classes_text, intro_text, menu_text
from classes.hunter_class import Hunter
from classes.item_class import Item
from classes.local_class import Local
from classes.weapon_class import Weapon
from data.classes_data import origens
from data.items_data import converte_efeito_json
from data.local_data import rua_abandonada
from game_functions import explore, shop, show_atributes, show_inventory
from utils import esperar, limpar, pedir_inteiro


def intro():
    limpar()

    print(titulo_ascii)

    print(intro_text)


def criar_personagem():
    print(criar_personagem_ascii)

    nome = input("Nome: ")
    idade = pedir_inteiro("Idade: ", range(1, 1000))
    print(classes_text)
    resposta = pedir_inteiro(validador=origens)

    hunter_obj = Hunter(nome, idade, r=resposta)
    print()

    print("==Personagem criado==")
    esperar()
    limpar()
    return hunter_obj


def main(personagem: Hunter, lugar: Local):
    while True:
        if personagem.hp <= 0:
            limpar()
            print(derrota_ascii)
            print("Você morreu")
            esperar()
            limpar()
            break

        print(menu_ascii)
        print(menu_text)

        r = pedir_inteiro(validador=range(1, 10))

        match r:
            case 1:
                limpar()
                explore(personagem, lugar)

            case 2:
                limpar()
                show_atributes(personagem)

            case 3:
                limpar()
                show_inventory(personagem)

            case 4:
                limpar()
                if personagem.inventario == []:
                    print("Inventario vazio")
                    esperar()
                else:
                    personagem.use_item()
                limpar()

            case 5:
                limpar()
                shop(personagem)

            case 9:
                limpar()
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
                print(fim_de_jogo_ascii)
                break


# Checar se save existe e ler save.
if Path("save.json").exists():
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
else:
    intro()
    personagem = criar_personagem()
    lugar = Local(rua_abandonada)

main(personagem, lugar)
