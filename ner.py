from flair.data import Sentence
from flair.models import SequenceTagger

from typing import List, Dict


class FlairNER:
    """
    This is a helper class that assists in retrieving the named entities from a given corpus
    """

    def __init__(self, model_name: str):
        self.ner_model = SequenceTagger.load(model_name)

    def get_entities(self, text: str, confidence: float) -> List[Dict]:
        """
        Function that returns the entities from a given text
        :param text: Input text
        :param confidence: a cutoff value for the ner confidence
        :return: a list of found ner entries
        """
        ner_entities = []

        decap_text = " ".join([word.lower().capitalize() if not word.islower() else word for word in text.split(" ")])
        tokenized_text = Sentence(decap_text)
        self.ner_model.predict(tokenized_text)
        # Entity text, label, position & score extraction
        for entity in tokenized_text.get_spans('ner'):
            if entity.tag not in ['MISC'] and entity.score >= confidence:
                ner_entities.append({"token": entity.text, "tag": entity.tag, "start_pos": entity.start_position,
                                     "end_pos": entity.end_position, "confidence_score": entity.score})
        return ner_entities
