import json
from pathlib import Path

schemas = Path("sirius_platform/contracts/schemas")

for f in schemas.glob("*.json"):
    try:
        json.loads(f.read_text())
        print(f"[OK] {f.name}")
    except Exception as e:
        print(f"[FAIL] {f.name} -> {e}")
