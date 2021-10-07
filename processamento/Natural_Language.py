import json
from typing import NewType

try:
    import models.Application_Exceptions as Application_Exceptions
except ModuleNotFoundError:
    from .models import Application_Exceptions 


"""
TODO:
• Refatorar código para não se repetir. Usar comprehensions ✖
• Aumentar lista de palavras com contexto (__atribuir_contexto) ✖
• Errors do nível baixo e escalar eles
• Validar dados (não deixar "" ser processado por exemplo)
• Melhorar respostas
"""

polaridade = NewType('Polaridade', int)
indice_confianca = NewType('Indice de confianca', [float or str])
try:
    with open('./processamento/nlp_database.json', 'r', encoding='utf-8') as json_file:
        dados = json.load(json_file)
except FileNotFoundError:
    with open('backend/processamento/nlp_database.json', 'r', encoding='utf-8') as json_file:
        dados = json.load(json_file)
class NLP(object):
    nlp_instace = NewType('nlp_instace', object)

    """
    (PT-BR) Classe básica. Aceita apenas um argumento que é a frase (do tipo str) a ser processada e retorna
    um JSON com os dados do processamento da frase 

    (EN) Basic class. Accepts only one argument the phrase itself (str type) 
    the phrase is processed and then it returns a JSON with the processed data.
    """

    def __init__(self, frase:str) -> nlp_instace:

        self.frase = frase
        self.process: object = self.__processar()
        if len(frase) == 0:
            raise Application_Exceptions.NoPhraseProvided("Insira uma frase!")
        
    def __separar_frase(self):
        polaridade = 0 #Lista que conterá a polaridade de cada palavra, para posteriormente obter o total, como neutro, positivo ou negativo
        unknow_words = 0    #Palavras desconhecidas é importante sua contagem, pois, dessa forma um indice de confiança fica mais preciso
        know_words= 0       #Palavras conhecidas, mesma razão das palavras desconhecidas
        
        lista_palavra = self.frase.split()

        for word in lista_palavra:
            
            actual_word = dados.get(word)
            
            if actual_word is not None:

                for value in actual_word.values():
                    
                    polaridade += value
                    know_words += 1
                    
            else:
                
                unknow_words += 1
                polaridade += 0
        
        json_file.close()       

        return [polaridade, know_words, unknow_words]

    def __indice_de_confianca(self, phrase_list: list, know_words: list) -> indice_confianca:
        if know_words > 0:

            total_words = len(phrase_list.split()) #mover para processos iniciais <-*
            cf =  f'{round(know_words / total_words *100)}%'

        else:
            cf = 'Baseado nos dados já coletados não posso chegar numa conclusão precisa'

        return cf

    def __atribuir_contexto(self, phrase_list:list, overallpolarity:int) -> indice_confianca:

        score = 0

        negative_context = ['não', 'nao', 'Não', 'Nao']
        neutral_context = ['que', 'Que']
        palavras_neutras = ['gostei', 'gosto'] # <- AQUI!!!!!

        phrase_list = phrase_list.split()

        if any(palavra in phrase_list for palavra in palavras_neutras): # <- Abordagem correta! 
            
            context1 = int([phrase_list.index(palavra) for palavra in palavras_neutras if palavra in phrase_list][0]) - 1
            if phrase_list[context1] in negative_context:
                score -= 1
            elif phrase_list[context1] in neutral_context:
                score += 0
            else:
                score += 1
        
        overallpolarity += score

        return overallpolarity

    def __resumo(self,score:int, cf:float, tw:int, uw:int, msg:str) -> object:
   
        retorno: object = {
            
                
                "Polaridade":score,
                "Confianca":cf, 
                "NumeroPalavras":tw,
                "PalavrasCon": tw - uw, 
                "PalavrasDesc":uw, 
                "Mensagem":msg,
                "Frase": self.frase
                
                }

        return retorno

    def __processar(self) -> nlp_instace:
    
        #Análise da polaridade da frase e atribuição de variáveis úteis
        nlp_instance = self.__separar_frase()

        #Atualizar o score através das variáveis de contexto
        contextscore = self.__atribuir_contexto(self.frase, nlp_instance[0])

        #Calcular o índice de confiança
        cf = self.__indice_de_confianca(self.frase, nlp_instance[1])

        #Criação da mensagem de análise de polaridade sentimental da frase
        if contextscore > 0:
            msg = f'A frase "{self.frase}" é positiva'
        elif contextscore == 0:
            msg = f'A frase "{self.frase}" é neutra'
        else:
            msg = f'A frase "{self.frase}" é negativa'

        nut = self.__resumo(contextscore, cf, len(self.frase.split()), nlp_instance[2], msg)

        return nut


    def __repr__(self) -> str:
        return f'(frase= {self.frase})'

if __name__ == "__main__":
    
    a1 = NLP('Que gosto ruim').process
    print(a1)
