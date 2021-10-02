#FastApi Stuff
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import socket

# Core do processamento
from processamento.Natural_Language import NLP

#Responses and other imports
from models.Response import Response
from models.Phrase import ProccessPhrase

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

@app.post('/processing')
def proc_phrase(phrase: ProccessPhrase):
    processed_response = NLP(phrase.phrase).process
  
    return Response(200, processed_response)

@app.get('/test/{phrase}')
def debg(phrase):
    processed_response = NLP(phrase).process
  
    return Response(200, processed_response)
