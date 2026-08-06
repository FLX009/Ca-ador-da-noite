class Weapon:
    def __init__(self, info):
        self.nome = info["nome"]
        self.dano = info["dano"]
        self.descricao = info["descricao"]

    def to_dict(self):
        """Transformar objeto em dicionario para json.dump()."""
        return {"nome": self.nome, "dano": self.dano, "descricao": self.descricao}
