from fastapi import FastAPI
from pydantic import BaseModel
from llm_guard.input_scanners import PromptInjection, Toxicity, Secrets,BanTopics

app = FastAPI()

class Request(BaseModel):
    message: str

@app.post("/guardrail")
def check_guardrail(req: Request):

    scanners = [
        PromptInjection(),
        Toxicity(),
        Secrets(),
        BanTopics(topics=["bomb", "explosive", "weapon", "attack", "terror"])
    ]

    text = req.message.lower()
    valid = True

    # run llm-guard scanners
    for scanner in scanners:
        sanitized_text, is_valid, _ = scanner.scan(text)
        if not is_valid:
            valid = False

    # 🚨 dangerous instruction filter
    dangerous_keywords = [
        "bomb",
        "explosive",
        "weapon",
        "terror",
        "attack"
    ]

    # 🚨 custom SQL protection
    dangerous_patterns = [
        "drop table",
        "delete from",
        "truncate table",
        "alter table",
        "shutdown database"
    ]

    for pattern in dangerous_patterns + dangerous_keywords:
        if pattern in text:
            valid = False

    return {
        "safe": valid,
        "message": req.message
    }