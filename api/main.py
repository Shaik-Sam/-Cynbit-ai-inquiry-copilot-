from typing import Optional

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from cynbit_copilot import CopilotPipeline

app = FastAPI(title="Cynbit Inquiry Copilot", version="0.1.0")
pipeline = CopilotPipeline()


class InquiryRequest(BaseModel):
    text: str = Field(min_length=3, max_length=4000)
    sender_name: Optional[str] = None


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/analyze")
def analyze(request: InquiryRequest):
    try:
        return pipeline.analyze(request.text, request.sender_name).to_dict()
    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc))
