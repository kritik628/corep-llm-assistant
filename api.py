from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from engine.retriever import simple_retrieve
from engine.generator import generate_corep_output
from engine.validator import validate_corep_output
from engine.mapper import map_to_template
from engine.rules_validator import check_consistency
from engine.audit import generate_audit_log

app = FastAPI(title="COREP LLM Reporting Assistant")

class CorepRequest(BaseModel):
    question: str
    scenario: str

@app.get("/")
def root():
    return {"message": "COREP LLM Assistant API is running"}

@app.post("/generate-corep")
def generate_corep(request: CorepRequest):
    try:
        retrieved = simple_retrieve(request.question)

        result = generate_corep_output(
            query=request.question,
            scenario=request.scenario,
            retrieved_rules=retrieved
        )

        is_valid, error = validate_corep_output(result)

        if not is_valid:
            raise HTTPException(status_code=400, detail=f"Schema validation failed: {error}")

        template_view = map_to_template(result)
        issues = check_consistency(result)
        audit_log = generate_audit_log(result)

        return {
            "structured_output": result,
            "template_view": template_view,
            "consistency_issues": issues,
            "audit_log": audit_log
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
