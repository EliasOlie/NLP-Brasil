#FastApi Stuff
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

#Libs
import json
from datetime import datetime
import os

# Core do processamento
from processamento.Natural_Language import NLP

#Responses and other imports
from models.Phrase import ProccessPhrase
from utils.makeissue import make_issue
from models.Response import Response
from models.ReviewPhrase import ReviewPhrase

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

@app.post('/stack/review')
def review_phrase(phrase: ReviewPhrase):
    token = os.getenv("GH_TOKEN")
    
    make_issue(token, phrase.phrase, phrase.comment)

    return Response(200)