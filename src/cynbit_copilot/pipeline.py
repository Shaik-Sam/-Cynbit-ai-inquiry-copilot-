from . import config
from .classifier import IntentClassifier, train_and_evaluate
from .data_gen import write_dataset
from .drafter import draft_reply
from .retriever import KnowledgeRetriever
from .schemas import Analysis
from .scoring import extract_entities, priority_score, priority_tier


def ensure_model():
    if config.MODEL_PATH.exists():
        return IntentClassifier.load()
    df = write_dataset()
    clf, _ = train_and_evaluate(df)
    clf.save()
    return clf


class CopilotPipeline:
    def __init__(self, classifier=None, retriever=None):
        self.classifier = classifier or ensure_model()
        self.retriever = retriever or KnowledgeRetriever()

    def analyze(self, text, sender_name=None):
        cleaned = " ".join(text.split())
        if not cleaned:
            raise ValueError("text must not be empty")
        intent, probs = self.classifier.predict(cleaned)
        confidence = probs[intent]
        entities = extract_entities(cleaned)
        score = priority_score(intent, confidence, entities)
        recommendations = self.retriever.search(cleaned, intent)
        reply, source = draft_reply(cleaned, intent, recommendations, entities, sender_name)
        low_confidence = confidence < config.CONFIDENCE_THRESHOLD
        return Analysis(
            text=cleaned,
            intent=intent,
            confidence=round(confidence, 4),
            probabilities={k: round(v, 4) for k, v in probs.items()},
            entities=entities,
            priority_score=score,
            priority_tier=priority_tier(score),
            route_to="Human Review Queue" if low_confidence else config.INTENT_TO_TEAM[intent],
            needs_human_review=low_confidence,
            recommendations=recommendations,
            draft_reply=reply,
            draft_source=source,
            sender_name=sender_name,
        )
