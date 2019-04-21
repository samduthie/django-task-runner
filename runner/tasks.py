import dramatiq


@dramatiq.actor(max_retries=0)
def test_task():
    print("test")
