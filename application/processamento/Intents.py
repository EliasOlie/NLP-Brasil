from operator import index
from typing import NewType

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
    
    def __init__(self, phrase:str, collection: list) -> IntentInstance:
        self.phrase = phrase
        self.collection = collection
        self.phrase_list = self.phrase.split()
        self.proccess = self.__proccess()

        if len(phrase) == 0:
            raise Application_Exceptions.NoPhraseProvided()
   
    def __extract_intents(self): # Refactor
        lista_prob = [get_probability(dictionary['Frase'], self.phrase)for dictionary in self.collection]
        provavel = [lista_prob.index(prob) for prob in lista_prob if prob > 0 and prob >= 0.5]
        resultados = [{"Intenção":self.collection[index(prob)]["Tipo"], "Probablilidade": lista_prob[prob]} for prob in provavel]

        polaridade = Natural_Language.NLP(self.phrase).proccess["Mensagem"]
        if len(provavel) == 0:
            resultados.append("Sem dados o suficiente para trazer um resultado confiável 🤖 considere cadastrar essas intenções no endpoint /stack/review/intent")
        return {"Resultado": resultados, "Polaridade": polaridade}   

    def __proccess(self) -> intent_type:
        return self.__extract_intents()

if __name__ == '__main__':
    data = [
        {'Frase': 'Ola', 'Tipo': 'Saudação'},
        {'Frase': 'Tcau', 'Tipo': 'Finalização'},
        {'Frase': 'Thca', 'Tipo': 'Finalização'},
        {'Frase': 'Quanto custa?', 'Tipo': 'Informação sobre preço'},
        {'Frase': 'Quamto cusa?', 'Tipo': 'Informação sobre preço'},
        {'Frase': 'Amei o ', 'Tipo': 'Elogio'},
        {'Frase': 'Ameri o ', 'Tipo': 'Elogio'},
        {'Frase': 'Olá gostaria de saber quanto custa', 'Tipo': 'Informação sobre preço'},
        {'Frase': 'Ola gotaria de saber qanto custa', 'Tipo': 'Informação sobre preço'}
    ]

    
    a = Intent("Olá", data).proccess
    print(a)
