import pytest

from cynbit_copilot import config
from cynbit_copilot.classifier import IntentClassifier, train_and_evaluate
from cynbit_copilot.data_gen import generate
from cynbit_copilot.pipeline import CopilotPipeline
from cynbit_copilot.retriever import KnowledgeRetriever
from cynbit_copilot.scoring import extract_entities, priority_score, priority_tier


@pytest.fixture(scope="module")
def pipeline():
    df = generate(samples_per_label=150)
    clf, _ = train_and_evaluate(df)
    return CopilotPipeline(classifier=clf, retriever=KnowledgeRetriever())


def test_dataset_balanced():
    df = generate(samples_per_label=20)
    assert set(df["label"]) == set(config.LABELS)
    assert df["label"].value_counts().nunique() == 1


def test_training_quality():
    _, metrics = train_and_evaluate(generate(samples_per_label=150))
    assert metrics["accuracy"] > 0.9
    assert metrics["macro_f1"] > 0.9


def test_entities():
    e = extract_entities("Need a portal in 6 weeks, budget Rs. 5,00,000, mail me at a@b.com ASAP")
    assert e.emails == ["a@b.com"]
    assert e.budgets
    assert e.timelines
    assert e.urgent


def test_priority_ordering():
    rich = extract_entities("Budget $8000, deadline 2 weeks, urgent")
    empty = extract_entities("hello")
    assert priority_score("project_inquiry", 0.9, rich) > priority_score("career_inquiry", 0.9, empty)
    assert priority_tier(0.8) == "high"
    assert priority_tier(0.55) == "medium"
    assert priority_tier(0.1) == "low"


def test_retriever_respects_intent():
    r = KnowledgeRetriever()
    for rec in r.search("learn data science", "learning_inquiry"):
        assert rec.category == "learning"


@pytest.mark.parametrize(
    "text,expected",
    [
        ("We need a mobile app built in 2 months with a budget of Rs. 3 lakh", "project_inquiry"),
        ("I am a fresher and want to learn Python, which course should I join", "learning_inquiry"),
        ("When will the internship assessment results be announced for my application", "career_inquiry"),
        ("Our college wants to collaborate with you on a hackathon", "partnership_inquiry"),
        ("I cannot log in, password reset email never arrives", "support_request"),
    ],
)
def test_intents(pipeline, text, expected):
    assert pipeline.analyze(text).intent == expected


def test_empty_rejected(pipeline):
    with pytest.raises(ValueError):
        pipeline.analyze("   ")


def test_model_roundtrip(tmp_path):
    clf, _ = train_and_evaluate(generate(samples_per_label=60))
    path = clf.save(tmp_path / "m.joblib")
    loaded = IntentClassifier.load(path)
    assert loaded.predict("need a website built")[0] == clf.predict("need a website built")[0]
