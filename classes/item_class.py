class Item:
    def __init__(self, info, quantos = 1):
        self.nome = info["nome"]
        self.descricao = info["descricao"]
        self.efeito = info["efeito"]
        self.preco = info["preco"]
        self.qtd_efeito = info["qtd_efeito"]
        self.quantidade = quantos