import json

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from . import config
from .schemas import Recommendation


class KnowledgeRetriever:
    def __init__(self, kb_path=config.KB_PATH):
        with open(kb_path, encoding="utf-8") as handle:
            self.items = json.load(handle)
        corpus = [self._document(item) for item in self.items]
        self.vectorizer = TfidfVectorizer(ngram_range=(1, 2), sublinear_tf=True, stop_words="english")
        self.matrix = self.vectorizer.fit_transform(corpus)

    @staticmethod
    def _document(item):
        return " ".join([item["name"], item["name"], item["summary"], " ".join(item["keywords"])])

    def search(self, text, intent, top_k=3):
        allowed = config.INTENT_TO_CATEGORIES.get(intent)
        scores = cosine_similarity(self.vectorizer.transform([text]), self.matrix)[0]
        ranked = sorted(range(len(self.items)), key=lambda i: scores[i], reverse=True)
        results = []
        for idx in ranked:
            item = self.items[idx]
            if allowed and item["category"] not in allowed:
                continue
            results.append(
                Recommendation(
                    id=item["id"],
                    name=item["name"],
                    category=item["category"],
                    summary=item["summary"],
                    score=round(float(scores[idx]), 4),
                )
            )
            if len(results) == top_k:
                break
        return results
