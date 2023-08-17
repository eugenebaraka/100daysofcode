import time
import datetime


def countdown(m, s):

    pomodoro_duration = datetime.timedelta(minutes=m, seconds=s)
    total_seconds_required = pomodoro_duration.total_seconds()

    while total_seconds_required > 0:
        timer = datetime.timedelta(total_seconds_required)
        print(timer)

        time.sleep(1)

        total_seconds_required -= 1

    print("0:00:00")


countdown(5, 0)