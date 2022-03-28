import pytest
import json

try:
    from Intents import Intent
except ModuleNotFoundError:
    from .Intents import Intent

try:
    import models.Application_Exceptions as Application_Exceptions
except ModuleNotFoundError:
    from .models import Application_Exceptions

test_col = [
    {"Frase":"Ola", "Tipo":"Saudação"},
    {"Frase":"Tcau", "Tipo":"Finalização"},
    {"Frase":"Thca", "Tipo":"Finalização"},
    {"Frase":"Quanto custa?", "Tipo":"Informação sobre preço"},
    {"Frase":"Quamto cusa?", "Tipo":"Informação sobre preço"},
    {"Frase":"Amei o ", "Tipo":"Elogio"},
    {"Frase":"Ameri o ", "Tipo":"Elogio"},
    {"Frase":"Olá gostaria de saber quanto custa","Tipo":"Informação sobre preço"},
    {"Frase":"Ola gotaria de saber qanto custa","Tipo":"Informação sobre preço"}
]

def test_evaluate(): 
    true_test = 0
    
    try:
        with open('./application/processamento/intents_test.json', 'r', encoding='utf-8') as json_file:
            dados:dict = json.load(json_file)
    except FileNotFoundError:
        with open('backend/application/processamento/intents_test.json', 'r', encoding='utf-8') as json_file:
            dados:dict = json.load(json_file)
    
    for phrase, sentiment in dados.items():
        test_proccess = Intent(phrase, test_col).proccess

        if test_proccess['Resultado'][0]['Intenção'] == sentiment["Tipo"]:
            true_test += 1
        else:
            true_test -= 1

    assert true_test == len(dados)

def test_no_phrase():
    with pytest.raises(Application_Exceptions.NoPhraseProvided) as exc_info:
        Intent("", test_col).proccess
    assert exc_info.type is Application_Exceptions.NoPhraseProvided

def test_no_confidence():
    if Intent("azangara", test_col).proccess["Resultado"][0] == "Sem dados o suficiente para trazer um resultado confiável 🤖 considere cadastrar essas intenções no endpoint /stack/review/intent":
        assert True
    else:
        assert False

test_evaluate()
test_no_phrase()
test_no_confidence()