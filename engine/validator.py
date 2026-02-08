import json
import os
from jsonschema import validate, ValidationError

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SCHEMA_PATH = os.path.join(BASE_DIR, "schemas", "corep_c0100_schema.json")

def validate_corep_output(data: dict):
    with open(SCHEMA_PATH, "r", encoding="utf-8") as f:
        schema = json.load(f)

    try:
        validate(instance=data, schema=schema)
        return True, None
    except ValidationError as e:
        return False, str(e)
