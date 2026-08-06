class Item:
    def __init__(self, info, quantos=1):
        self.nome = info["nome"]
        self.descricao = info["descricao"]
        self.efeito = info["efeito"]
        self.preco = info["preco"]
        self.qtd_efeito = info["qtd_efeito"]
        self.quantidade = quantos

    def to_dict(self):
        """Transformar objeto em dicionario para json.dump()."""
        return {
            "nome": self.nome,
            "descricao": self.descricao,
            "efeito": self.efeito.__name__,
            "preco": self.preco,
            "qtd_efeito": self.qtd_efeito,
            "quantidade": self.quantidade,
        }
