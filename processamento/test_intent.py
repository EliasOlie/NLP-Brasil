import pytest
import json

try:
    import Intents
except ModuleNotFoundError:
    from . import Intents

try:
    import models.Application_Exceptions as Application_Exceptions
except ModuleNotFoundError:
    from .models import Application_Exceptions

def test_evaluete():
    true_test = 0
    
    try:
        with open('./processamento/intents_test.json', 'r', encoding='utf-8') as json_file:
            dados:dict = json.load(json_file)
    except FileNotFoundError:
        with open('backend/processamento/intents_test.json', 'r', encoding='utf-8') as json_file:
            dados:dict = json.load(json_file)
    
    for phrase, sentiment in dados.items():
        test_process = Intents.Intent(phrase).process

        if test_process["Resultado"][-1:][0]["Intenção"]["Tipo"] == sentiment["Tipo"]:
            true_test += 1
        else:
            true_test -= 1

    assert true_test == len(dados)

def test_no_phrase():
    with pytest.raises(Application_Exceptions.NoPhraseProvided) as exc_info:
        Intents.Intent("").process
    assert exc_info.type is Application_Exceptions.NoPhraseProvided

def test_no_confidence():
    if Intents.Intent("azangara").process["Resultado"][0] == "Sem dados o suficiente para trazer um resultado confiável 🤖 considere cadastrar essas intenções no endpoint /stack/review/intent":
        assert True
    else:
        assert False

test_evaluete()
test_no_phrase()
test_no_confidence()