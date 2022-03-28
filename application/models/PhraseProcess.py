from typing import Any
from pydantic import BaseModel
  
class PolarityReq(BaseModel):
    phrase: str
    
class PolarityRes(BaseModel):
    proccess: Any