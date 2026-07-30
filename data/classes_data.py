from data import weapons_data

sobrevivente = {
    "atributos": {"HP": 10 , 'STR': 10, 'DEF': 8, 'AGL': 1, 'INT': 1},
    "qtd_moedas": 10,
    "arma": weapons_data.machadinha,
    "origem": "Sobrevivente"
}

soldado = {
    "atributos": {"HP": 8 , 'STR': 8, 'DEF': 5, 'AGL': 8, 'INT': 1},
    "qtd_moedas": 20,
    "arma": weapons_data.espada,
    "origem": "Soldado"
}

estudioso = {
    "atributos": {"HP": 5, 'STR': 1, 'DEF': 8, 'AGL': 1, 'INT': 15},
    "qtd_moedas": 20,
    "arma": weapons_data.cajado,
    "origem": "Estudioso"
}

cacador = {
    "atributos": {"HP": 10 , 'STR': 1, 'DEF': 8, 'AGL': 10, 'INT': 1},
    "qtd_moedas": 30,
    "arma": weapons_data.lanca,
    "origem": "Caçador"
}

origens = {
    1: sobrevivente,
    2: soldado,
    3: estudioso,
    4: cacador
}