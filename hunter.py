import weapon

class hunter_class:
    def __init__(self, nome, idade, resposta):
        self.nome = nome
        self.idade = idade
        self.arma = None
        self.origem = None
        self.qtd_moedas = 0
        self.atributos = {}

        match resposta:
            case (1):
                self.atributos = {"HP": 7 , 'STR': 7, 'DEF': 6, 'AGL': 5, 'INT': 5}
                self.qtd_moedas = (10)
                self.arma = weapon.weapon_class("Machadinha", (2, 5), "Uma ferramenta de trabalho transformada em arma de sobrevivência.")
                self.origem = 'Sobrevivente'

            case (2):
                self.atributos = {"HP": 8 , 'STR': 10, 'DEF': 8, 'AGL': 3, 'INT': 1}
                self.qtd_moedas = (20)
                self.arma = weapon.weapon_class("Espada", (4, 6), "Uma lâmina confiável, feita para enfrentar qualquer ameaça.")
                self.origem = 'Soldado'

            case (3):
                self.atributos = {"HP": 4, 'STR': 2, 'DEF': 6, 'AGL': 6, 'INT': 12}
                self.qtd_moedas = (20)
                self.arma = weapon.weapon_class("Cajado", (5, 9), "Um simples bastão que esconde antigos poderes.")
                self.origem = 'Estudioso'

            case (4):
                self.atributos = {"HP": 6 , 'STR': 5, 'DEF': 5, 'AGL': 10, 'INT': 4}
                self.qtd_moedas = (30)
                self.arma = weapon.weapon_class("Lança", (4, 6), "Uma arma de alcance, criada para manter o perigo longe.")
                self.origem = 'Caçador'