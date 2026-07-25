import os
import time
from ascii import menu_ascii, criar_personagem_ascii, titulo_ascii
from classes.hunter_class import hunter
from classes.local_class import local
from data.local_data import rua_abandonada
from functions import show_atributes, explore, show_inventory, shop

def intro():
    os.system("cls")

    print(titulo_ascii)

    print("""
            Quando a noite caiu sobre a cidade, o mundo que existia antes desapareceu
            As ruas foram tomadas por criaturas vindas de lugares esquecidos
            e aquilo que um dia foi lar tornou-se um território de medo e morte
            Cercado pela escuridão e sem saber o que espreita além das sombras
            um morador precisa encontrar forças para sobreviver até o amanhecer
            enquanto a cidade lentamente se perde para uma presença que ninguém consegue compreender
            
            """)

def criar_personagem():
    print(criar_personagem_ascii)
  
    nome = input("Nome: ")
    idade = input("Idade: ")
    print("Origem: ")
    print("[1] Sobrevivente com Machadinha")
    print("[2] Soldado com Espada")
    print("[3] Estudioso com Cajado")
    print("[4] Caçador com Lança")
    resposta = int(input())
    
    hunter_obj = hunter(nome, idade, resposta)
    print()

    print("==Personagem criado==")
    time.sleep(2)
    os.system("cls")
    return hunter_obj

def main(personagem: hunter, lugar: local):
        
        
        while True:
            print(menu_ascii)
            
            print("""            [1]Explorar
            [2]Ver Atributos
            [3]Ver Inventario
            [4]Usar Item
            [5]Loja
            [6]Melhorar Personagem
            [7]Descansar
            [8]Enfrentar Chefe
            [9]Encerrar jogo""")

            r = int(input())

            match r:
                case 1:
                    explore(personagem, lugar)

                case 2: 
                    show_atributes(personagem)

                case 3:
                    show_inventory(personagem)

                case 5:
                    shop()


    



intro()
personagem = criar_personagem()
lugar = local(rua_abandonada)
main(personagem, lugar)