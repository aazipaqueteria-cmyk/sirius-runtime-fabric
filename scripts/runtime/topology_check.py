from pathlib import Path

required = [
    "sirius_platform/runtime_fabric",
    "sirius_platform/contracts",
    "sirius_platform/testing",
    "sirius_platform/observability",
]

for r in required:

    if Path(r).exists():
        print(f"[OK] {r}")
    else:
        print(f"[FAIL] missing {r}")
