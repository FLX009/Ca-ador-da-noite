from classes.weapon_class import weapon
from data import weapons_data

class hunter:
    def __init__(self, nome, idade, resposta):
        self.nome = nome
        self.idade = idade
        self.arma = None
        self.origem = None
        self.qtd_moedas = 0
        self.atributos = {}
        self.inventario = []

        match resposta:
            case (1):
                self.atributos = {"HP": 10 , 'STR': 10, 'DEF': 8, 'AGL': 1, 'INT': 1}
                self.qtd_moedas = (10)
                self.arma = weapon(weapons_data.machadinha)
                self.origem = 'Sobrevivente'

            case (2):
                self.atributos = {"HP": 8 , 'STR': 8, 'DEF': 5, 'AGL': 8, 'INT': 1}
                self.qtd_moedas = (20)
                self.arma = weapon(weapons_data.espada)
                self.origem = 'Soldado'

            case (3):
                self.atributos = {"HP": 5, 'STR': 1, 'DEF': 8, 'AGL': 1, 'INT': 15}
                self.qtd_moedas = (20)
                self.arma = weapon(weapons_data.cajado)
                self.origem = 'Estudioso'

            case (4):
                self.atributos = {"HP": 10 , 'STR': 1, 'DEF': 8, 'AGL': 10, 'INT': 1}
                self.qtd_moedas = (30)
                self.arma = weapon(weapons_data.lanca)
                self.origem = 'Caçador'