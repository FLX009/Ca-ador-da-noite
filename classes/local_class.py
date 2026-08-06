class Local:
    def __init__(self, info):
        self.nome = info["nome"]
        self.inimigos = info["inimigos"]

    def to_dict(self):
        """Transformar objeto em dicionario para json.dump()."""
        return {"nome": self.nome, "inimigos": self.inimigos}
