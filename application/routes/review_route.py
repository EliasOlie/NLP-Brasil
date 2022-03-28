from fastapi import APIRouter
from fastapi.responses import JSONResponse
import os

from application.models.ReviewPhrase import ReviewPhrase
from application.models.ReviewIntent import ReviewIntent
from application.utils.makeissue import make_issue
from application.utils.update_file import update_review_file

review_router = APIRouter(
    prefix='/review',
    tags=['GitHub review', "Phrase review", "Intent review"]
)

@review_router.post('/stack/review')
def review_phrase(phrase: ReviewPhrase):
    token = os.getenv("GH_TOKEN")
    
    make_issue(token, phrase.phrase, phrase.comment)

    return JSONResponse(status_code=200)

@review_router.post('/stack/review/intents')
def review_phrase(data: ReviewIntent):
    token = os.getenv("GH_TOKEN")

    update_review_file(token, 'processamento/intents_review.json', data.data)

    return JSONResponse(status_code=200)