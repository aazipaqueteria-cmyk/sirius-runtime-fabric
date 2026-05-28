from platform.runtime.executor.runtime_executor import RuntimeExecutor

def test_runtime_execution():

    r = RuntimeExecutor()

    result = r.execute({
        "tenant":"enterprise",
        "task":"inference"
    })

    assert result["status"] == "accepted"
