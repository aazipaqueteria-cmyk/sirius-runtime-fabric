bootstrap:
\tpython3 -m venv .venv && . .venv/bin/activate && pip install -r requirements.lock.txt

test:
\t. .venv/bin/activate && pytest

contracts:
\t. .venv/bin/activate && python scripts/governance/validate_contracts.py

topology:
\t. .venv/bin/activate && python scripts/runtime/topology_check.py

runtime-health:
\tbash scripts/bootstrap/runtime_healthcheck.sh
