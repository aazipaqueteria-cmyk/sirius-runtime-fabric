from sirius_platform.runtime_mesh.queue.runtime_queue import RuntimeQueue

def test_queue():

    q = RuntimeQueue()

    q.enqueue("job")

    assert q.size() == 1
