import sys
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
from classes.local_class import Local
from data.classes_data import origens
from data.local_data import rua_abandonada
from game_functions import (
    delete_save,
    explore,
    load_save,
    save,
    shop,
    show_atributes,
    show_inventory,
)
from utils import esperar, limpar, pedir_inteiro


def intro():
    limpar()

    print(titulo_ascii)

    print(intro_text)

    r = pedir_inteiro("[1] Criar personagem ou [2] Fechar jogo: ", range(1, 3))

    if r == 2:
        sys.exit()


def criar_personagem():
    limpar()
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


def inicializacao():
    intro()
    personagem = criar_personagem()
    lugar = Local(rua_abandonada)
    return personagem, lugar


def main(personagem: Hunter, lugar: Local):
    while True:
        if personagem.hp <= 0:
            limpar()
            print(derrota_ascii)
            print(f"{' '*18}Você morreu")
            esperar()
            limpar()

            while True:
                r = pedir_inteiro("[1]Recarregar save ou [2]Sair: ", range(1, 3))

                if r == 1:
                    personagem, lugar = load_save()
                    if personagem is not None:
                        break
                else:
                    sys.exit()

        print(menu_ascii)
        print(menu_text)

        r = pedir_inteiro(validador=range(1, 13))

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
                if Path("save.json").exists():
                    personagem, lugar = load_save()
                    print("save carregado!")
                    esperar()
                    limpar()
                else:
                    print("Não existe um save")
                    esperar()

            case 10:
                limpar()
                save(personagem, lugar)
                print("Jogo salvo!")
                esperar()

            case 11:
                limpar()
                save(personagem, lugar)
                print(fim_de_jogo_ascii)
                break

            case 12:
                limpar()
                deletado = delete_save()
                if deletado:
                    personagem, lugar = inicializacao()


# Checar se save existe e ler save.
if Path("save.json").exists():
    personagem, lugar = load_save()
    limpar()
    print(titulo_ascii)
    print(f"{' '*18}Save carregado!")
    esperar()
    limpar()
else:
    personagem, lugar = inicializacao()

main(personagem, lugar)
