from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from custom_typing import *
from ner import FlairNER

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# INIT: loading required models for NER -> these models are loaded from a shared mount.
ner_model = FlairNER("/models/NER-model")


@app.get("/", response_model=health_response, name="Health check route")
async def root():
    """
    This function is a simple health check --> Could be relevant if you are using liveliness/readiness checks.
    """
    return {"status": "healthy"}


@app.get("/get_ner_entities", response_model=ner_entities_response,
         name="This route is made to get the NER's for a document")
async def get_ner_entities(input_text: str, confidence_score: float = 0.6):
    """
    This function extract the Named entities from a file and returns them.

    :param input_text: The content of a file
    :param confidence_score: a threshold for the confidence from the NER
    :return: a dict formatted list of NER entities that were found from the text
    """
    ner_entities = ner_model.get_entities(text=input_text, confidence=confidence_score)
    return {"result": ner_entities}
