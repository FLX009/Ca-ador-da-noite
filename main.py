from utils import limpar, esperar, pedir_inteiro
from assets.text import intro_text, classes_text, menu_text
from assets.ascii import menu_ascii, criar_personagem_ascii, titulo_ascii, fim_de_jogo_ascii, derrota_ascii
from classes.hunter_class import Hunter
from classes.local_class import Local
from data.classes_data import origens   
from data.local_data import rua_abandonada
from game_functions import show_atributes, explore, show_inventory, shop

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
    
    hunter_obj = Hunter(nome, idade, resposta)
    print("")

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

            r = pedir_inteiro(validador = range(1, 10))

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
                    personagem.use_item()

                case 5:
                    limpar()
                    shop(personagem)

                case 9:
                    limpar()
                    print(fim_de_jogo_ascii)
                    break

intro()
personagem = criar_personagem()
lugar = Local(rua_abandonada)
main(personagem, lugar)