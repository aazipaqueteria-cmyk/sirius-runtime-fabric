from sirius_platform.runtime_execution.state_machine.runtime_state_machine import RuntimeStateMachine

def test_transition():

    sm = RuntimeStateMachine()

    assert sm.transition("running") is True
