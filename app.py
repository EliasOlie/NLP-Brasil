# FastApi Stuff
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Libs
import os
from application.models.ReviewIntent import ReviewIntent


# Core do processamento
from application.processamento.Natural_Language import NLP
from application.processamento.Intents import Intent

# Routes
from application.routes.phrase_route import phrase_router

# Responses and other imports
from application.models.Intent import ProcessIntent
from application.utils.makeissue import make_issue
from application.utils.update_file import update_review_file
from application.models.Response import Response
from application.models.ReviewPhrase import ReviewPhrase
import application.processamento.models.Application_Exceptions
import application.models.errors as API_ERR

app = FastAPI()

#CORS Policy
origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(phrase_router)

# @app.get('/')
# def landing():
#     return {"Message":'Olá! para processar frases faça um post no endpoint "/processing"', "error": False}

# @app.post('/processing')
# def proc_phrase(phrase: ProccessPhrase):
#     try:
#         processed_response = NLP(phrase.phrase).process
#         return Response(200, processed_response)
#     except application.processamento.models.Application_Exceptions.NoPhraseProvided:
#         return Response(422, API_ERR.NO_PHRASE_PROVIDED, True)


# @app.get('/test/{phrase}')
# def debg(phrase):
#     try:
#         processed_response = NLP(phrase).process
#         return Response(200, processed_response)
#     except application.processamento.models.Application_Exceptions.NoPhraseProvided:
#         return Response(422, API_ERR.NO_PHRASE_PROVIDED, True)

# @app.post('/intent')
# def intent_processing(phrase: ProcessIntent):
#     col = IntentsDB.read({"user": "U1"}, {"_id": 0})['Intents']
#     try:
#         proc_response = Intent(phrase.phrase, col).process
#         return Response(200, proc_response)
#     except application.processamento.models.Application_Exceptions.NoPhraseProvided:
#         return(422, API_ERR.NO_PHRASE_PROVIDED, True)

# @app.post('/stack/review')
# def review_phrase(phrase: ReviewPhrase):
#     token = os.getenv("GH_TOKEN")
    
#     make_issue(token, phrase.phrase, phrase.comment)

#     return Response(200)

# @app.post('/stack/review/intents')
# def review_phrase(data: ReviewIntent):
#     token = os.getenv("GH_TOKEN")

#     update_review_file(token, 'processamento/intents_review.json', data.data)

#     return Response(200)