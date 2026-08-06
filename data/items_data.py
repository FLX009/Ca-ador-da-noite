def curar(personagem, quantidade):
    """Efeito de cura."""
    personagem.hp += quantidade
    personagem.hp = min(personagem.atributos["max HP"], personagem.hp)


converte_efeito_json = {
    "curar": curar,
}

pocao = {
    "nome": "Poção",
    "descricao": "Cura 8 HP",
    "efeito": curar,
    "qtd_efeito": 8,
    "preco": 10,
}
