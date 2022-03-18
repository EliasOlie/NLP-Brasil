from fastapi import APIRouter
from fastapi.responses import JSONResponse
from application.models.PhraseProcess import PhraseReq, PhraseRes
from application.processamento.Natural_Language import NLP

phrase_router = APIRouter(
    prefix='/phrase',
    tags=['Phrase process']
)

@phrase_router.post('/sentiment')
def process_sentiment(request: PhraseReq):
    proc = NLP(request.data).process
    res: PhraseRes = {"usr_api": request.usr_api, "process_output": proc}
    return JSONResponse(status_code=200, content=res)