from data import classes_data
from classes.weapon_class import Weapon
from utils import esperar
import random

class Hunter:
    def __init__(self, nome, idade, resposta):
        self.nome = nome
        self.idade = idade
        self.hp = 0
        self.arma = None
        self.origem = None
        self.qtd_moedas = 0
        self.atributos = {}
        self.inventario = []

        classe_escolhida = classes_data.origens[resposta]

        self.arma = Weapon(classe_escolhida["arma"])
        self.origem = classe_escolhida["origem"]
        self.qtd_moedas = classe_escolhida["qtd_moedas"]
        self.atributos = classe_escolhida["atributos"].copy()
        self.hp = self.atributos["max HP"]

    def atacar(self):
        dano_final = random.randint(*self.arma.dano)
        return dano_final

    def use_item(self, em_luta = False):
        itens_inventario = set()
        for i in self.inventario:
            print(f"{i.nome} x{i.quantidade}")
            itens_inventario.add(i.nome)

        resposta = input("Escreva o nome do item para usar: ")

        if resposta in itens_inventario:
            for i in self.inventario:
                if i.nome == resposta:
                    i.efeito(self, i.qtd_efeito)
                    if i.quantidade == 1:
                        self.inventario.remove(i)
                    else:
                        i.quantidade -= 1
                    print("Item usado.")
                    usado = True
                    esperar()
                    break
        
        else:
            print("Item não encontrado")
            esperar()
            if em_luta is True:
                self.use_item(em_luta = True)