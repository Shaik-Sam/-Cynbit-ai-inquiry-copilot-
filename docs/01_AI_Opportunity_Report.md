# AI Opportunity Report for Cynbit

Prepared by Shaik Samiulla for the AI/ML Engineer Intern assessment.

## 1. Scope and sources

This report is based on the public Cynbit website structure and the candidate application portal. Observed public surface areas:

- Company: Our Story, Our Team, Careers, Social Impact
- Expertise: Services Hub, Product Suite, Case Studies
- BitElevate ecosystem: Learning Paths, Student Diaries
- Blog and newsletter (the footer advertises 25k+ subscribers)
- Contact and "Get Started Now" entry points, three phone lines and a shared opportunities mailbox
- A staged application hub with application screening and a technical assessment phase
- Headquarters in Jaipur, Rajasthan

Specific service names, pricing and internal volumes are not public, so figures below are labelled assumptions. The knowledge base in the prototype is illustrative and is meant to be replaced with Cynbit's real catalogue.

## 2. Business model read-out

Cynbit appears to run three connected engines:

1. Services and products for business clients (engineering, product suite, case studies).
2. BitElevate, a learning ecosystem that trains students and feeds talent back into the company.
3. Community and brand (blog, newsletter, student diaries, social impact).

Every engine begins with an inbound human message: a project inquiry, a learner question, an application, a partnership proposal or a support issue. These arrive through the same few channels, so the quality of the first response drives conversion in all three engines.

## 3. Industry context

- Software services firms in India compete on speed of response and proposal quality. Slow replies to inbound leads are one of the most common causes of lost deals.
- Edtech and skilling programmes depend on personalised guidance, since learners drop out when they cannot see a clear path.
- Early-stage hiring through assessments produces large applicant volumes where manual screening does not scale.
- Generative AI and retrieval-augmented systems now make it practical for a small team to run grounded assistants over its own content at low cost.
- India's Digital Personal Data Protection Act, 2023 makes consent, purpose limitation and data minimisation design requirements for any system handling applicant or learner data.

## 4. Opportunity long-list

| # | Opportunity | Engine | Description |
|---|---|---|---|
| 1 | Inquiry Triage and Response Copilot | All | Classify inbound messages, extract budget and timeline, score priority, route to the right team, recommend offerings, draft a grounded first reply |
| 2 | Personalised BitElevate Learning Path Recommender | BitElevate | Recommend paths from goals and skill level, plus dropout-risk prediction and nudges |
| 3 | Assessment Screening Assistant | Careers | Rubric-based scoring support for technical task submissions and resumes, with human decision |
| 4 | Website RAG Assistant | All | Conversational assistant grounded in services, case studies, blog and learning paths |
| 5 | Proposal and Case-Study Generator | Services | Retrieve similar past case studies and generate proposal drafts and estimates |
| 6 | Content Intelligence for Blog and Newsletter | Community | Topic mining, SEO suggestions, segment-based newsletter personalisation |
| 7 | Social Impact Analytics | Community | Outcome tracking and reporting across skilling programmes |

## 5. Prioritisation

Scores are 1 to 5 (5 is best). Weights: business impact 35%, feasibility for a small team 25%, data readiness 20%, risk (higher is safer) 10%, time to value 10%.

| # | Impact | Feasibility | Data readiness | Risk | Time to value | Weighted |
|---|---|---|---|---|---|---|
| 1 | 5 | 5 | 4 | 4 | 5 | 4.75 |
| 2 | 4 | 4 | 3 | 4 | 3 | 3.75 |
| 3 | 3 | 4 | 3 | 2 | 4 | 3.30 |
| 4 | 4 | 4 | 4 | 3 | 4 | 3.95 |
| 5 | 4 | 3 | 2 | 3 | 2 | 3.15 |
| 6 | 2 | 5 | 4 | 5 | 4 | 3.65 |
| 7 | 2 | 3 | 2 | 4 | 2 | 2.55 |

## 6. Selected opportunity: Inquiry Triage and Response Copilot

### Why this one

- It sits at the entry of all three engines, so one system benefits sales, BitElevate admissions, talent acquisition, partnerships and support.
- Cynbit's own contact points and application hub generate the data needed, and a safe cold start is possible with synthetic data and a curated knowledge base.
- It keeps a human in control: the system drafts and routes, people approve.
- It can ship as an API or a form plug-in in a few weeks and also becomes the foundation for opportunity 4 (RAG assistant) and opportunity 5.

### Problem statement

Messages from clients, learners, candidates and partners are read manually, answered inconsistently and prioritised by whoever happens to see them first. High-value leads and urgent support issues wait in the same queue as routine questions.

### Proposed solution

A pipeline that, for each inbound message:

1. Detects intent: project, learning, career, partnership, support.
2. Extracts budget, timeline, contact details and urgency.
3. Computes a transparent priority score and tier.
4. Routes to the owning team, or to human review when confidence is low.
5. Retrieves the most relevant Cynbit offerings.
6. Drafts a grounded reply for a human to approve.

### Success metrics

| Metric | Baseline (assumed) | Target after pilot |
|---|---|---|
| Median first response time | Hours | Under 15 minutes for high priority |
| Routing accuracy | Manual, unmeasured | 90% or higher on audited sample |
| Lead-to-call conversion | Current rate | Relative lift of 15% |
| Agent time per message | Current | 40% reduction |
| Draft acceptance without edit | Not applicable | 60% or higher |

### Risks and mitigations

| Risk | Mitigation |
|---|---|
| Wrong routing | Confidence threshold, human review queue, weekly audit |
| Hallucinated commitments in drafts | Grounded context only, prompt prohibits prices and dates, human approval |
| Personal data exposure | Minimal logging, masking of emails in logs, consent notice, DPDP-aligned retention |
| Bias against some applicants or regions | Priority score uses only transparent, non-personal features; periodic fairness review |
| Model drift | Monitor class distribution and confidence, retrain monthly from corrected labels |

### Roadmap beyond the prototype

Phase 2: RAG assistant over case studies and blog. Phase 3: learner path recommender and dropout alerts. Phase 4: proposal generator using retrieval over past projects.
