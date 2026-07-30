from classes.hunter_class import Hunter
from classes.local_class import Local
from classes.enemy_class import Enemy
from utils import pedir_inteiro, limpar, esperar
from assets.ascii import fight_ascii, escapou_ascii, vitoria_ascii, derrota_ascii
from assets.text import fight_options_text
from data import items_data
import random

def explore(personagem: Hunter, lugar: Local):
    limpar()
    
    r = random.randint(0, 5)

    match r:
        #inimigo
        case 0:
            inimigos_possiveis = len(lugar.inimigos)-1
            inimigo_escolhido = lugar.inimigos[random.randint(0, inimigos_possiveis)]
            inimigo = Enemy(inimigo_escolhido)

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

def show_atributes(personagem: Hunter):
    limpar()

    for k, v in personagem.atributos.items():
        print(f"{k} : {v}")

def show_inventory(personagem: Hunter):
    limpar()

    print(personagem.inventario)
    print(f"Moedas: {personagem.qtd_moedas}")

def shop():
    print(items_data.pocao)

def fight(personagem: Hunter, inimigo: Enemy):
    primeiro_turno = True
    defendeu = False
    K = 8

    while True:
        if inimigo.hp <= 0:             #checar se inimigo morreu
            limpar()
            print(vitoria_ascii)
            print(f"{inimigo.nome} derrotado")
            esperar()
            limpar()
            break

        if not primeiro_turno:              #não deixar inimigo bater no primeiro turno
            dano_inimigo = inimigo.atacar()             #dano do inimigo


            if defendeu is True:                #calcular dano do inimigo quando defender
                dano_final = dano_inimigo * (1 - reducao)
                personagem.atributos["HP"] -= dano_final
                print(f"Você defendeu {dano_inimigo - dano_final} de dano.")
                esperar()
                defendeu = False
            else:
                dano_final = dano_inimigo
                personagem.atributos["HP"] -= dano_inimigo              #dano do inimigo sem defender

            print(f"{inimigo.nome} causou {dano_final} de dano.")
            esperar()

        primeiro_turno = False

        if personagem.atributos["HP"] <= 0:             #checar se player morreu
            limpar()
            print(derrota_ascii)
            print("Você morreu")
            esperar()
            limpar
            break
        
        print(fight_ascii)              #informaçoes do combate
        print(f"{personagem.nome} {" "* 25} {inimigo.nome}")
        print(f"HP: {personagem.atributos["HP"]} {" "* 25} HP: {inimigo.hp}")
        print(personagem.arma.nome)
        print("")
        print(fight_options_text)

        resposta = pedir_inteiro(validador = range(1,5))

        match resposta:
            case 1:             #atacar
                dano_player = personagem.atacar()
                inimigo.hp -= dano_player
                limpar()
                print(f"{personagem.nome} causou {dano_player} de dano.")
                esperar()

            case 2:             #defender
                defendeu = True
                reducao = personagem.atributos["DEF"]/(personagem.atributos["DEF"] + K)
                limpar()

            case 3:             #item
                pass

            case 4:             #escapar
                chance = random.randint(1, 10)
                if chance == 1:
                    limpar()
                    print(escapou_ascii)
                    esperar()
                    break
                limpar()
                print("escapar falhou")
                limpar()