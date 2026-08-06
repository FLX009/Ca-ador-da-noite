import random

from classes.weapon_class import Weapon
from data import classes_data
from utils import esperar


class Hunter:
    def __init__(
        self,
        nome,
        idade,
        hp=0,
        origem=None,
        arma=None,
        qtd_moedas=0,
        atributos=None,
        r=None,
    ):
        self.nome = nome
        self.idade = idade
        self.hp = hp
        self.arma = arma
        self.origem = origem
        self.qtd_moedas = qtd_moedas
        self.atributos = atributos
        self.inventario = []

        if r is not None:
            classe_escolhida = classes_data.origens[r]

            self.arma = Weapon(classe_escolhida["arma"])
            self.origem = classe_escolhida["origem"]
            self.qtd_moedas = classe_escolhida["qtd_moedas"]
            self.atributos = classe_escolhida["atributos"].copy()
            self.hp = self.atributos["max HP"]

    def to_dict(self):
        """Transformar objeto em dicionario para json.dump()."""
        dict_inventario = [item.to_dict() for item in self.inventario]
        return {
            "nome": self.nome,
            "idade": self.idade,
            "hp": self.hp,
            "qtd_moedas": self.qtd_moedas,
            "origem": self.origem,
            "atributos": self.atributos,
            "inventario": dict_inventario,
        }

    def atacar(self):
        """Calcular dano."""
        dano_final = random.randint(*self.arma.dano)
        return dano_final

    def use_item(self, em_luta=False):
        """Usar item."""
        itens_inventario = set()
        for i in self.inventario:
            print(f"{i.nome} x{i.quantidade}")
            itens_inventario.add(i.nome)

        r = input("Escreva o nome do item para usar: ")

        if r in itens_inventario:
            for i in self.inventario:
                if i.nome == r:
                    i.efeito(self, i.qtd_efeito)
                    if i.quantidade == 1:
                        self.inventario.remove(i)
                    else:
                        i.quantidade -= 1
                    print("Item usado.")
                    esperar()
                    break

        else:
            print("Item não encontrado")
            esperar()
            if em_luta is True:
                self.use_item(em_luta=True)
