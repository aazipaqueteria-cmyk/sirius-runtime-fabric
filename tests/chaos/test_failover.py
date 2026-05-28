from sirius_platform.runtime_mesh.failover.failover_engine import FailoverEngine

def test_failover():

    e = FailoverEngine()

    result = e.recover("node-a")

    assert result["status"] == "recovered"
