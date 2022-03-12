import pymongo
from decouple import config

PSW = config("MONGO_PASS")
USR = config("MONGO_USR")

class DB:

    """
    TODO:
        Classe? OK! ✔
        Context Managers? Not needed ✖
        Excepions! NEXT! 
    """
    def __init__(self, db:str, collection:str):
        self.client = pymongo.MongoClient(f"mongodb+srv://{USR}:{PSW}@cluster0.dnxkm.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
        self.db = self.client[db]
        self.collection = self.db[collection]
        
    def isalive(self):
        try:
            self.client.admin.command('ismaster')
            return "Connected"
        
        except Exception as e:
            print("Not connected", e)

    def create(self, data: dict) -> 0|1:
        self.collection.insert_one(data)
        return 0

    def read(self, selector: dict, projection:dict=None) -> dict|None:
        data:dict|None = self.collection.find_one(selector, projection,no_cursor_timeout=False)
        return data

    def update(self, selector: dict, data: dict) -> int:
        change = self.collection.update_one(selector, data)
        return change.modified_count

    def delete(self, selector: dict) -> int:
        deletion = self.collection.delete_one(selector)
        return deletion.deleted_count

if __name__ == '__main__':
    test = DB("NLP-Core", "Intents")
    print(test.isalive())