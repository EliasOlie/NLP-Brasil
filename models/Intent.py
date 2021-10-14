from pydantic import BaseModel

class ProcessIntent(BaseModel):
    phrase: str