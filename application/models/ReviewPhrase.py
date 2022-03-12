from pydantic import BaseModel
from typing import Optional

class ReviewPhrase(BaseModel):
    phrase: str
    comment: Optional[str] = "Nenhum comentário provido"
