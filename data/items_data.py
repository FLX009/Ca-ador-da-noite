def curar(personagem, quantidade):
    personagem.hp += quantidade
    if personagem.hp >= personagem.atributos["max HP"]:
        personagem.hp = personagem.atributos["max HP"]

pocao = {
    "nome": "Poção",
    "descricao": "Cura 8 HP",
    "efeito": curar,
    "qtd_efeito": 8,
    "preco": 10
}