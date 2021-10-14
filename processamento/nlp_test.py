# coding=<utf-8>    

import pytest

try:
    import models.Application_Exceptions as Application_Exceptions
except ModuleNotFoundError:
    from .models import Application_Exceptions 


try:
    import Natural_Language
except ModuleNotFoundError:
    from . import Natural_Language
import json

"""
Creio que uma análise básica na polaridade é, pelo menos à principio o sulficiente para
testar, porém, em breve teremos mais regras à seguir que demandarão mais testes

"""

def test_main():
    true_test = 0

    with open('./processamento/dataset_test.json', 'r', encoding='utf8') as file:
        testes = json.load(file)
    
    for test_phrase, test_value in testes.items():
        teste_process = Natural_Language.NLP(test_phrase).process     

        retorno = teste_process["Polaridade"]       
        
        if test_value["Polaridade"] == retorno:
            true_test += 1
        else:
            true_test -= 1


    assert true_test == len(testes)

def test_no_phrase_provided():
    with pytest.raises(Application_Exceptions.NoPhraseProvided) as exc_info:
        Natural_Language.NLP("").process
    assert exc_info.type is Application_Exceptions.NoPhraseProvided


test_main()
test_no_phrase_provided()
