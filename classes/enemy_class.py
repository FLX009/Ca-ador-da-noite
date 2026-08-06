import random


class Enemy:
    def __init__(self, info):
        self.nome = info["nome"]
        self.dano = info["dano"]
        self.max_hp = info["max HP"]
        self.hp = self.max_hp
        self.moedas = info["moedas"]

    def atacar(self):
        dano_final = random.randint(*self.dano)
        return dano_final
