from sirius_platform.runtime_fabric.dispatchers.workload_dispatcher import WorkloadDispatcher

def test_dispatch():

    dispatcher = WorkloadDispatcher()

    result = dispatcher.dispatch({
        "tenant":"enterprise"
    })

    assert result == "isolated-cluster"
