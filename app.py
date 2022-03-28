# FastApi Stuff
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Routes
from application.routes.polarity_route import polarity_router
from application.routes.intent_route import intent_router
from application.routes.review_route import review_router


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

app.include_router(polarity_router)
app.include_router(intent_router)
app.include_router(review_router)

@app.get('/')
def landing():
    return {"Message":'Olá! para processar frases faça um post no endpoint "/processing"', "error": False}



