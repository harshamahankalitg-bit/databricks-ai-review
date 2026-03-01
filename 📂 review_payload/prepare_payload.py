import json
from pathlib import Path

def prepare():

    code = Path("src/job.py").read_text()
    coverage = Path("coverage.json").read_text()

    payload = {
        "code": code,
        "coverage": coverage
    }

    return json.dumps(payload)
