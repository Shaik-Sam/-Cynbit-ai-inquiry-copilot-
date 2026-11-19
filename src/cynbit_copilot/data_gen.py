import random

import pandas as pd

from . import config

COMPANIES = ["fintech startup", "retail chain", "logistics company", "healthcare clinic", "edtech startup", "manufacturing unit", "real estate firm", "D2C brand", "NGO", "hospitality group"]
DOMAINS = ["e-commerce", "healthcare", "logistics", "education", "finance", "travel", "retail", "agriculture"]
SERVICES = ["a customer portal", "a mobile app", "an inventory dashboard", "a booking platform", "an ERP integration", "a CRM system", "a cloud migration", "a data analytics dashboard", "a company website", "a security audit", "a chatbot for support", "workflow automation"]
ACTIONS = ["build a web application", "automate our reporting", "migrate to the cloud", "redesign our website", "develop an Android app", "set up a CI/CD pipeline", "run a penetration test"]
AI_FEATURES = ["a recommendation engine", "an AI chatbot", "demand forecasting", "document extraction", "fraud detection", "sentiment analysis"]
TIMELINES = ["2 weeks", "4 weeks", "6 weeks", "3 months", "2 months", "10 days", "one quarter", "ASAP", "end of this month"]
BUDGETS = ["Rs. 2,00,000", "INR 5 lakh", "$8000", "Rs. 75,000", "around 3 lakh", "$15k", "Rs. 10 lakh", "INR 1,50,000"]
STUDENT_TYPES = ["final year student", "second year B.Tech student", "fresher", "working professional", "diploma student", "MCA student"]
SKILLS = ["full stack development", "data science", "machine learning", "cloud and DevOps", "UI/UX design", "Python", "cybersecurity", "Java", "React", "generative AI"]
GOALS = ["campus placements", "an internship", "my first developer job", "a career switch", "higher studies"]
ROLES = ["AI/ML Engineer Intern", "Full Stack Developer Intern", "UI/UX Design Intern", "Data Analyst Intern", "DevOps Engineer", "Content Writer Intern", "Backend Developer"]
EXPERIENCE = ["no", "six months of", "one year of", "two years of"]
ORGS = ["engineering college", "tech community", "NGO", "media company", "startup accelerator", "training institute", "software company"]
COLLABS = ["a joint hackathon", "campus workshops", "a skilling programme", "co-branded webinars", "a CSR initiative", "an internship pipeline", "a reseller agreement"]
THINGS = ["student dashboard", "login page", "course portal", "payment page", "client portal", "mobile app", "assessment portal", "invoice module"]
ERRORS = ["upload a file", "submit the form", "open the dashboard", "download the certificate", "make a payment", "reset my password"]
NAMES = ["Aarav", "Priya", "Samiulla", "Ananya", "Rohit", "Meera", "Karthik", "Fatima", "Vikram", "Sneha"]

TEMPLATES = {
    "project_inquiry": [
        "We are a {company} and need {service} built within {timeline}. Our budget is {budget}.",
        "Looking for a team to {action} for our {domain} business. Can we schedule a call this week?",
        "Need a quote for {service}. Deadline is {timeline}.",
        "Our {domain} startup wants to add {ai} to our product. What would it cost and how long would it take?",
        "We want to {action}. Budget is {budget} and we need delivery in {timeline}. Please share a proposal.",
        "Can Cynbit help our {company} with {service}? We need an estimate urgently.",
    ],
    "learning_inquiry": [
        "I am a {student} and want to learn {skill}. Which learning path should I pick?",
        "Do you offer a course on {skill} for beginners? How long does it take?",
        "Can I join BitElevate to prepare for {goal}? I know basic {skill}.",
        "What is the fee and duration of the {skill} program?",
        "As a {student}, I want a roadmap for {skill} to get {goal}. Any mentorship available?",
        "Are there batches starting soon for {skill}? I am preparing for {goal}.",
    ],
    "career_inquiry": [
        "I applied for the {role} position. When will the assessment results be announced?",
        "Are there openings for {role} at your company? I have {exp} experience.",
        "Sharing my resume for the {role} role, please let me know the next steps.",
        "What is the selection process for the {role} internship?",
        "I completed the technical task for {role}. How can I check my application status?",
        "Is the {role} internship paid and remote?",
    ],
    "partnership_inquiry": [
        "We are a {org} interested in collaborating with Cynbit on {collab}.",
        "Our {org} wants to partner for {collab}. Who should we speak to?",
        "Would you be open to {collab}? We believe it would benefit both organisations.",
        "As a {org}, we would like to explore {collab} with your team.",
        "We run a {org} and are looking for a long term partner for {collab}.",
    ],
    "support_request": [
        "The {thing} is not working. I get an error when I try to {error}.",
        "I cannot log in to the {thing}, the reset email never arrives.",
        "My payment went through but I did not get access to the {thing}.",
        "Facing a bug in the {thing} delivered last month, please fix it urgently.",
        "I am unable to {error} on the {thing}. It keeps crashing.",
        "The {thing} shows a blank page since yesterday and our team is blocked.",
    ],
}

PREFIXES = ["", "Hi team, ", "Hello, ", "Good morning, ", "Dear Cynbit team, ", "Hey, "]
SUFFIXES = ["", " Thanks.", " Regards, {name}", " Please reply at {email}.", " Looking forward to your response.", " Thank you!"]


def _fill(template, rng):
    values = {
        "company": rng.choice(COMPANIES),
        "domain": rng.choice(DOMAINS),
        "service": rng.choice(SERVICES),
        "action": rng.choice(ACTIONS),
        "ai": rng.choice(AI_FEATURES),
        "timeline": rng.choice(TIMELINES),
        "budget": rng.choice(BUDGETS),
        "student": rng.choice(STUDENT_TYPES),
        "skill": rng.choice(SKILLS),
        "goal": rng.choice(GOALS),
        "role": rng.choice(ROLES),
        "exp": rng.choice(EXPERIENCE),
        "org": rng.choice(ORGS),
        "collab": rng.choice(COLLABS),
        "thing": rng.choice(THINGS),
        "error": rng.choice(ERRORS),
    }
    return template.format(**values)


def _decorate(text, rng):
    name = rng.choice(NAMES)
    email = f"{name.lower()}{rng.randint(1, 99)}@example.com"
    suffix = rng.choice(SUFFIXES).format(name=name, email=email)
    out = rng.choice(PREFIXES) + text + suffix
    if rng.random() < 0.15:
        out = out.lower()
    if rng.random() < 0.1:
        out = out.replace(" the ", " ", 1)
    return out


def generate(samples_per_label=config.SAMPLES_PER_LABEL, seed=config.SEED):
    rng = random.Random(seed)
    rows = []
    for label, templates in TEMPLATES.items():
        for _ in range(samples_per_label):
            text = _decorate(_fill(rng.choice(templates), rng), rng)
            rows.append({"text": text, "label": label})
    rng.shuffle(rows)
    return pd.DataFrame(rows)


def write_dataset(path=config.DATASET_PATH):
    df = generate()
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False)
    return df
