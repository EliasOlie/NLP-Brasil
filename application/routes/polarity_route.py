from fastapi import APIRouter
from fastapi.responses import JSONResponse
from application.models.PhraseProcess import PolarityReq, PolarityRes
from application.processamento.models.Application_Exceptions import NoPhraseProvided
from application.models.errors import NO_PHRASE_PROVIDED 

from application.processamento.Natural_Language import NLP

polarity_router = APIRouter(
    prefix='/phrase',
    tags=['Phrase process']
)

@polarity_router.post('/polarity')
def proccess_polarity(req: PolarityReq):
    try:
        proc = NLP(req.phrase).proccess
        res: PolarityRes = {"proccess": proc}
        return JSONResponse(status_code=200, content=res)    
    except(NoPhraseProvided):
        return JSONResponse(status_code=400, content=NO_PHRASE_PROVIDED)
    