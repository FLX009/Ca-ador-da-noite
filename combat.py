import random

from assets.ascii import escapou_ascii, fight_ascii, vitoria_ascii
from assets.text import fight_options_text
from utils import esperar, limpar, pedir_inteiro


def fight(personagem: object, inimigo: object):
    invencivel = True
    defendeu = False
    reducao = 0
    K = 8

    while True:
        if inimigo.hp <= 0:  # checar se inimigo morreu
            limpar()
            print(vitoria_ascii)
            print(f"{inimigo.nome} derrotado")
            esperar()
            limpar()
            break

        if not invencivel:  # não deixar inimigo bater no primeiro turno
            dano_inimigo = inimigo.atacar()  # dano do inimigo

            if defendeu is True:  # calcular dano do inimigo quando defender
                dano_final = dano_inimigo * (1 - reducao)
                personagem.hp -= dano_final
                print(f"Você defendeu {dano_inimigo - dano_final} de dano.")
                esperar()
                defendeu = False
            else:
                dano_final = dano_inimigo
                personagem.hp -= dano_inimigo  # dano do inimigo sem defender

            print(f"{inimigo.nome} causou {dano_final} de dano.")
            esperar()

        invencivel = False

        if personagem.hp <= 0:  # checar se player morreu
            break

        print(fight_ascii)  # informaçoes do combate
        print(f"{personagem.nome} {' ' * 25} {inimigo.nome}")
        print(
            f"HP: {personagem.hp}/{personagem.atributos['max HP']} {' ' * 25} HP: {inimigo.hp}/{inimigo.max_hp}"
        )
        print(personagem.arma.nome)
        print()
        print(fight_options_text)

        resposta = pedir_inteiro(validador=range(1, 5))

        match resposta:
            case 1:  # atacar
                dano_player = personagem.atacar()
                inimigo.hp -= dano_player
                limpar()
                print(f"{personagem.nome} causou {dano_player} de dano.")
                esperar()

            case 2:  # defender
                defendeu = True
                reducao = personagem.atributos["DEF"] / (
                    personagem.atributos["DEF"] + K
                )
                limpar()

            case 3:  # item
                limpar()
                if personagem.inventario == []:
                    print("Inventario vazio")
                    invencivel = True
                    esperar()
                else:
                    personagem.use_item(em_luta=True)

            case 4:  # escapar
                chance = random.randint(1, 10)
                if chance in range(1, 3):
                    limpar()
                    print(escapou_ascii)
                    esperar()
                    limpar()
                    break
                limpar()
                print("escapar falhou")
                esperar()
                limpar()
