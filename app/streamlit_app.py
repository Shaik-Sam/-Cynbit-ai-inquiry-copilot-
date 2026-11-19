import pandas as pd
import streamlit as st

from cynbit_copilot import CopilotPipeline

SAMPLES = {
    "Project lead": "We are a logistics company and need an inventory dashboard built within 6 weeks. Our budget is Rs. 5,00,000. Please reply at ops@example.com.",
    "Learner": "I am a final year B.Tech student and want to learn machine learning. Which BitElevate learning path should I pick for placements?",
    "Candidate": "I completed the technical task for the AI/ML Engineer Intern role. How can I check my application status?",
    "Partnership": "Our engineering college wants to partner for campus workshops and a skilling programme. Who should we speak to?",
    "Support": "The client portal is not working and our team is blocked. It keeps crashing when we upload a file, please fix urgently.",
}

st.set_page_config(page_title="Cynbit Inquiry Copilot", layout="wide")


@st.cache_resource
def load_pipeline():
    return CopilotPipeline()


pipeline = load_pipeline()

st.title("Cynbit Inquiry Copilot")
st.caption("Intent detection, priority scoring, routing, recommendations and a reply draft for every inbound message.")

choice = st.selectbox("Load a sample inquiry", ["Custom"] + list(SAMPLES))
default_text = SAMPLES.get(choice, "")
text = st.text_area("Inbound message", value=default_text, height=150)
name = st.text_input("Sender name (optional)")

if st.button("Analyze", type="primary") and text.strip():
    result = pipeline.analyze(text, name or None)

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Intent", result.intent.replace("_", " ").title())
    c2.metric("Confidence", f"{result.confidence:.0%}")
    c3.metric("Priority", f"{result.priority_tier.upper()} ({result.priority_score})")
    c4.metric("Route to", result.route_to)

    if result.needs_human_review:
        st.warning("Confidence is below the threshold. This message is sent to human review.")

    left, right = st.columns(2)
    with left:
        st.subheader("Class probabilities")
        probs = pd.Series(result.probabilities).sort_values()
        st.bar_chart(probs)
        st.subheader("Extracted entities")
        st.json(
            {
                "emails": result.entities.emails,
                "budgets": result.entities.budgets,
                "timelines": result.entities.timelines,
                "urgent": result.entities.urgent,
            }
        )
    with right:
        st.subheader("Recommended offerings")
        st.dataframe(
            pd.DataFrame([r.__dict__ for r in result.recommendations])[["name", "category", "score", "summary"]],
            use_container_width=True,
            hide_index=True,
        )
        st.subheader(f"Draft reply ({result.draft_source})")
        st.text_area("Reply", value=result.draft_reply, height=260, label_visibility="collapsed")
