import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, f1_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline

from . import config


class IntentClassifier:
    def __init__(self):
        self.model = Pipeline(
            [
                ("tfidf", TfidfVectorizer(ngram_range=(1, 2), sublinear_tf=True, min_df=2, lowercase=True)),
                ("clf", LogisticRegression(max_iter=2000, class_weight="balanced", C=4.0)),
            ]
        )

    def fit(self, texts, labels):
        self.model.fit(texts, labels)
        return self

    def predict(self, text):
        probs = self.model.predict_proba([text])[0]
        classes = [str(c) for c in self.model.classes_]
        best = int(probs.argmax())
        return classes[best], {c: float(p) for c, p in zip(classes, probs)}

    def save(self, path=config.MODEL_PATH):
        path.parent.mkdir(parents=True, exist_ok=True)
        joblib.dump(self.model, path)
        return path

    @classmethod
    def load(cls, path=config.MODEL_PATH):
        instance = cls()
        instance.model = joblib.load(path)
        return instance


def train_and_evaluate(df, test_size=0.2, seed=config.SEED):
    x_train, x_test, y_train, y_test = train_test_split(
        df["text"], df["label"], test_size=test_size, random_state=seed, stratify=df["label"]
    )
    clf = IntentClassifier().fit(x_train, y_train)
    preds = clf.model.predict(x_test)
    labels = sorted(df["label"].unique())
    metrics = {
        "train_size": int(len(x_train)),
        "test_size": int(len(x_test)),
        "accuracy": float(accuracy_score(y_test, preds)),
        "macro_f1": float(f1_score(y_test, preds, average="macro")),
        "labels": labels,
        "confusion_matrix": confusion_matrix(y_test, preds, labels=labels).tolist(),
        "report": classification_report(y_test, preds, output_dict=True, zero_division=0),
    }
    return clf, metrics
