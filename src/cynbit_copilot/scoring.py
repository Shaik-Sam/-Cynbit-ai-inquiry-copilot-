import re

from .schemas import Entities

EMAIL_RE = re.compile(r"[\w.+-]+@[\w-]+\.[\w.-]+")
BUDGET_RE = re.compile(
    r"(?:rs\.?|inr|\$|usd|₹)\s?[\d,\.]+\s?(?:k|l|lakh|lakhs|cr|crore|m)?\b|\b[\d\.]+\s?(?:lakh|lakhs|crore|k)\b",
    re.IGNORECASE,
)
TIMELINE_RE = re.compile(
    r"\b\d+\s?(?:day|days|week|weeks|month|months)\b|\bone quarter\b|\bthis week\b|\bend of this month\b|\btomorrow\b|\basap\b",
    re.IGNORECASE,
)
URGENT_RE = re.compile(r"\burgent(?:ly)?\b|\basap\b|\bimmediately\b|\bblocked\b|\bcrash(?:es|ing)?\b|\bcritical\b", re.IGNORECASE)

INTENT_BASE = {
    "project_inquiry": 0.45,
    "support_request": 0.5,
    "partnership_inquiry": 0.35,
    "learning_inquiry": 0.25,
    "career_inquiry": 0.15,
}


def extract_entities(text):
    return Entities(
        emails=EMAIL_RE.findall(text),
        budgets=[m.strip() for m in BUDGET_RE.findall(text)],
        timelines=[m.strip() for m in TIMELINE_RE.findall(text)],
        urgent=bool(URGENT_RE.search(text)),
    )


def priority_score(intent, confidence, entities):
    score = INTENT_BASE.get(intent, 0.2)
    if entities.budgets:
        score += 0.2
    if entities.timelines:
        score += 0.12
    if entities.urgent:
        score += 0.15
    if entities.emails:
        score += 0.03
    score += 0.05 * confidence
    return round(min(score, 1.0), 3)


def priority_tier(score):
    if score >= 0.75:
        return "high"
    if score >= 0.5:
        return "medium"
    return "low"
