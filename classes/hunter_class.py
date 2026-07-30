from data import classes_data
from classes.weapon_class import Weapon
import random

class Hunter:
    def __init__(self, nome, idade, resposta):
        self.nome = nome
        self.idade = idade
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

    def atacar(self):
        dano_final = random.randint(*self.arma.dano)
        return dano_final