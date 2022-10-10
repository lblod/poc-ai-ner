from typing import List
from typing_extensions import TypedDict


class health_response(TypedDict):
    status: str


class ner_entities_response(TypedDict):
    class inner_ner_entities_response(TypedDict):
        token: str
        tag: str
        start_pos: int
        end_pos: int
        confidence_score: float

    result: List[inner_ner_entities_response]
