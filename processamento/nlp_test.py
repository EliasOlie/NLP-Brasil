# coding=<utf-8>    

import pytest
try:
    import Natural_Language
except ModuleNotFoundError:
    from . import Natural_Language
import json
# import Natural_Language
"""
TODO 

• Mover frases para um json com frases ✔

Invés de validar todos os dados de resposta, analisar apenas a polaridade, e talvez, o score.
O problema de testar o score é que conforme mais palavras forem sendo classificadas o número de palavras
conhecidas (que é uma variável para calcular o score) modificando assim o score e quebrando o teste;
a não ser que invés de colocar num dataset o valor esperado calcular com um fetch na api

"""
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
        
        # print(test_value, retorno)
        if test_value["Polaridade"] == retorno:
            true_test += 1
        else:
            true_test -= 1


    assert true_test == len(testes)

test_main()

"""
{'Polaridade': -1, 'Confidence': '75%', 'Numero de palavras': 4, 'Palavras desconhecidas': 1, 'Mensagem': 'A frase "não gostei do pão" é negativa'}
{'Polaridade': -1, 'Confidence': '75%', 'Numero de palavras': 4, 'Palavras desconhecidas': 1, 'Mensagem': 'a frase "não gostei do pão" e negativa'}

{'Polaridade': 1, 'Confidence': '75%', 'Numero de palavras': 4, 'Palavras desconhecidas': 1, 'Mensagem': 'A frase "gosto muito de você" é positiva'}
{'Polaridade': 1, 'Confidence': '75%', 'Numero de palavras': 4, 'Palavras desconhecidas': 1, 'Mensagem': 'A frase "gosto muito de você" é positiva'}

{'Polaridade': 1, 'Confidence': '67%', 'Numero de palavras': 3, 'Palavras desconhecidas': 1, 'Mensagem': 'A frase "gostei do livro" é positiva'}
{'Polaridade': 1, 'Confidence': '67%', 'Numero de palavras': 3, 'Palavras desconhecidas': 1, 'Mensagem': 'A frase "gostei do livro" é positiva'}
"""