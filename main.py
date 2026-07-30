from utils import limpar, esperar, pedir_inteiro
from assets.text import intro_text, classes_text, menu_text, fight_options_text
from assets.ascii import menu_ascii, criar_personagem_ascii, titulo_ascii, fim_de_jogo_ascii
from classes.hunter_class import Hunter
from classes.local_class import Local
from data.classes_data import origens
from data.local_data import rua_abandonada
from functions import show_atributes, explore, show_inventory, shop

def intro():
    limpar()

    print(titulo_ascii)

    print(intro_text)

def criar_personagem():
    print(criar_personagem_ascii)
  
    nome = input("Nome: ")
    idade = pedir_inteiro("Idade: ", range(1, 101))   
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
            print(menu_ascii)
            print(menu_text)

            r = pedir_inteiro(validador = range(1, 10))

            match r:
                case 1:
                    explore(personagem, lugar)

                case 2: 
                    show_atributes(personagem)

                case 3:
                    show_inventory(personagem)

                case 5:
                    shop()

                case 9:
                    limpar()
                    print(fim_de_jogo_ascii)
                    break

intro()
personagem = criar_personagem()
lugar = Local(rua_abandonada)
main(personagem, lugar)