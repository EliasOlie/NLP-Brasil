try:
    from .db import DB
except:
    from db import DB
    
IntentsDB = DB("NLP-Core", "Intents")

if __name__ == '__main__':
    i = {
    "Ola":{"Tipo":"Saudação"},
    "Tcau": {"Tipo":"Finalização"},
    "Thca": {"Tipo":"Finalização"},
    "Quanto custa?": {"Tipo":"Informação sobre preço"},
    "Quamto cusa?": {"Tipo":"Informação sobre preço"},
    "Amei o ": {"Tipo":"Elogio"},
    "Ameri o ": {"Tipo":"Elogio"},
    "Olá gostaria de saber quanto custa":{"Tipo":"Informação sobre preço"},
    "Ola gotaria de saber qanto custa":{"Tipo":"Informação sobre preço"}
    }
    # IntentsDB.create({"user": "U1", "Intents": []})
    # for k,v in i.items():
    #     for sk,sv in v.items():
    #         d = {"Frase": k, sk: sv}
    #         IntentsDB.update({"user": "U1"}, {"$push": {"Intents":d}})
    col = IntentsDB.read({"user": "U1"}, {"_id": 0})
    print(col['Intents'])
    