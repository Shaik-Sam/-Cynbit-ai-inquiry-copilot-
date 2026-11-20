# Execution Notes for the Portal

Project: Cynbit Inquiry Copilot, an AI system that triages every inbound message to Cynbit.

Selected opportunity: Inquiry triage and response copilot, chosen from seven opportunities after weighted scoring (see docs/01_AI_Opportunity_Report.md).

Architecture: TF-IDF and Logistic Regression intent classifier, regex entity extraction, transparent priority scorer, intent-filtered TF-IDF retrieval over a knowledge base, and an LLM reply drafter with a template fallback. Low-confidence messages go to human review.

Setup:

```
git clone https://github.com/Shaik-Sam/-Cynbit-ai-inquiry-copilot-
cd cynbit-ai-inquiry-copilot
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
python scripts/train.py
python scripts/evaluate.py
pytest -q
streamlit run app/streamlit_app.py
uvicorn api.main:app --reload
```

Optional LLM drafting: copy `.env.example` to `.env`, set `ANTHROPIC_API_KEY`, and export it. Without a key the template fallback is used.

Results: 1.00 accuracy on the synthetic hold-out and 0.89 on 19 hand-written messages. The gap is reported openly in the technical report along with the planned fixes.

Documents: docs/01_AI_Opportunity_Report.md, docs/02_Technical_Approach_Report.md.
