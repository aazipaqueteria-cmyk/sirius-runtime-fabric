from sirius_platform.runtime_status.api.system_status import SystemStatus

def test_status():

    s = SystemStatus()

    result = s.health()

    assert result["runtime"] == "active"
