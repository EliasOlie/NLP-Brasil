from typing import Any
from pydantic import BaseModel, Json

class PhraseReq(BaseModel):
    usr_api: str
    data: Any
    
class PhraseRes(BaseModel):
    usr_api: str
    process_output: Any
    
if __name__ == '__main__':
    d = {"usr_api": '1', "process_output": {'proc':"t"}}
    s = PhraseRes(**d).json()
    print(s)