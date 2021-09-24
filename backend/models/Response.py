import json

class Response():
    def __init__(self, status:int, data:object=None, error:bool=False) -> None:
        self.status = status
        self.data = data
        self.error = error

    def __repr__(self) -> object:
        return json.dumps({"Code":self.status, "Error":self.error, "data":self.data}, ensure_ascii=False)