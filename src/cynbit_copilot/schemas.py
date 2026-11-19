from dataclasses import asdict, dataclass, field
from typing import Dict, List, Optional


@dataclass
class Entities:
    emails: List[str] = field(default_factory=list)
    budgets: List[str] = field(default_factory=list)
    timelines: List[str] = field(default_factory=list)
    urgent: bool = False


@dataclass
class Recommendation:
    id: str
    name: str
    category: str
    summary: str
    score: float


@dataclass
class Analysis:
    text: str
    intent: str
    confidence: float
    probabilities: Dict[str, float]
    entities: Entities
    priority_score: float
    priority_tier: str
    route_to: str
    needs_human_review: bool
    recommendations: List[Recommendation]
    draft_reply: str
    draft_source: str
    sender_name: Optional[str] = None

    def to_dict(self):
        return asdict(self)
