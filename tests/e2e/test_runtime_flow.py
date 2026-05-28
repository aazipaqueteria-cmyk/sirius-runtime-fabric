from sirius_platform.runtime_mesh.loadbalancer.runtime_lb import RuntimeLoadBalancer

def test_lb():

    lb = RuntimeLoadBalancer()

    result = lb.select(["node-a","node-b"])

    assert result == "node-a"
