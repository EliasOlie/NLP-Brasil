from typing import NewType
import json

from difflib import SequenceMatcher

try:
    import Natural_Language
except ModuleNotFoundError:
    from . import Natural_Language

try:
    import models.Application_Exceptions as Application_Exceptions
except ModuleNotFoundError:
    from .models import Application_Exceptions 

intent_type = NewType("Intent", object)
IntentInstance = NewType("Intent" , object)

def get_probability(palavra_correta: str, palavra_enviada: str) -> float:
    
    return SequenceMatcher(None, palavra_correta, palavra_enviada).ratio()

class Intent:
    
    def __init__(self, phrase:str) -> IntentInstance:
        self.phrase = phrase
        self.phrase_list = self.phrase.split()
        self.process = self.__process()

        if len(phrase) == 0:
            raise Application_Exceptions.NoPhraseProvided()

    def __extract_intents(self):
        try:
            with open('./processamento/intents.json', 'r', encoding='utf-8') as json_file:
                dados:dict = json.load(json_file)
        except FileNotFoundError:
            with open('backend/processamento/intents.json', 'r', encoding='utf-8') as json_file:
                dados:dict = json.load(json_file)

        lista_prob = [get_probability(key, self.phrase) for key in dados.keys()]
        provavel = [lista_prob.index(prob) for prob in lista_prob if prob > 0 and prob >= 0.5]
        lista_index = [key for key in dados.keys()]
        resultados = [{"Intenção": dados.get(lista_index[prob]), "Probabilidade": lista_prob[prob]} for prob in provavel]

        polaridade = Natural_Language.NLP(self.phrase).process["Mensagem"]
        if len(provavel) == 0:
            resultados.append("Sem dados o suficiente para trazer um resultado confiável 🤖 considere cadastrar essas intenções no endpoint /stack/review/intent")
        return {"Resultado": resultados, "Polaridade": polaridade}   

    def __process(self) -> intent_type:
        return self.__extract_intents()

if __name__ == '__main__':
    a = Intent("Ola").process
    print(a)#["Resultado"][-1:][0]["Intenção"]["Tipo"]