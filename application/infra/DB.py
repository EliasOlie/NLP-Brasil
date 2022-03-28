import os
import pymongo
from decouple import config

try:
    CONNECTION_URL = os.environ["DB_LINK"]
except KeyError:
    CONNECTION_URL = config("DB_LINK")

class DB:

    """
    TODO:
        Classe? OK! ✔
        Context Managers? Not needed ✖
        Excepions! NEXT! 
    """
    def __init__(self, db:str, collection:str):
        self.client = pymongo.MongoClient(CONNECTION_URL)
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
    test = DB("NLP", "Intents")
    print(test.isalive())