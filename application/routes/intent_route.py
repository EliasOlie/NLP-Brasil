from fastapi import APIRouter
from fastapi.responses import JSONResponse
from application.processamento.Intents import Intent
from application.processamento.models.Application_Exceptions import NoPhraseProvided
from application.models.Intent import ProcessIntent
from application.models.errors import NO_PHRASE_PROVIDED 
from application.infra.DB import DB

IntentsDB = DB("NLP", "Intents")

intent_router = APIRouter(
    prefix='/intent',
    tags=["Intent review"]
)

@intent_router.post('/intent')
def intent_processing(phrase: ProcessIntent):
    col = IntentsDB.read({"user": "U1"}, {"_id": 0})['Intents'] # WORK in progress!
    try:
        proc_response = Intent(phrase.phrase, col).process
        return JSONResponse(status_code=200, content=proc_response)
    except NoPhraseProvided:
        return JSONResponse(status_code=422, contet=NO_PHRASE_PROVIDED)