import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = ROOT / "data"
MODEL_DIR = ROOT / "models"
REPORT_DIR = ROOT / "reports"
KB_PATH = DATA_DIR / "knowledge_base.json"
DATASET_PATH = DATA_DIR / "synthetic_inquiries.csv"
MODEL_PATH = MODEL_DIR / "intent_model.joblib"
METRICS_PATH = REPORT_DIR / "metrics.json"

LABELS = [
    "project_inquiry",
    "learning_inquiry",
    "career_inquiry",
    "partnership_inquiry",
    "support_request",
]

INTENT_TO_CATEGORIES = {
    "project_inquiry": ["service", "product"],
    "learning_inquiry": ["learning"],
    "career_inquiry": ["career"],
    "partnership_inquiry": ["impact", "partnership"],
    "support_request": ["support"],
}

INTENT_TO_TEAM = {
    "project_inquiry": "Sales and Solutions",
    "learning_inquiry": "BitElevate Admissions",
    "career_inquiry": "Talent Acquisition",
    "partnership_inquiry": "Partnerships and Impact",
    "support_request": "Customer Success",
}

SEED = 42
SAMPLES_PER_LABEL = 400
CONFIDENCE_THRESHOLD = float(os.getenv("CYNBIT_CONFIDENCE_THRESHOLD", "0.45"))
LLM_MODEL = os.getenv("CYNBIT_LLM_MODEL", "claude-sonnet-4-6")
