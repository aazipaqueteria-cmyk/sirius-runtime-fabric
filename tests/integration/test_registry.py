from sirius_platform.runtime_mesh.service_registry.registry import ServiceRegistry

def test_registry():

    r = ServiceRegistry()

    r.register("api","10.0.0.1")

    assert r.resolve("api") == "10.0.0.1"
