from sirius_platform.runtime_execution.dag.runtime_dag import RuntimeDAG

def test_dag():

    dag = RuntimeDAG()

    dag.add_task("task-a")

    assert len(dag.tasks()) == 1
