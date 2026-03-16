from celery import shared_task
import time


@shared_task(bind=True)
def long_running_task(self, duration):

    for i in range(duration):
        time.sleep(1)

        self.update_state(
            state="PROGRESS",
            meta={
                "current": i + 1,
                "total": duration
            }
        )

    return {
        "current": duration,
        "total": duration,
        "status": "completed"
    }
