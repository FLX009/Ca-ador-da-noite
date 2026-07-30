import random

class Enemy:
    def __init__(self, info):
        self.nome = info["nome"]
        self.dano = info["dano"]
        self.hp = info["HP"]
        self.moedas = info["moedas"]

    def atacar(self):
        dano_final = random.randint(*self.dano)
        return dano_final