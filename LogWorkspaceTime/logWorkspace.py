import os
import json
from time import sleep
from datetime import timedelta, date

WORKSPACE_CMD = "wmctrl -d | grep '*' | cut -d ' ' -f1"
TIME_FILE = 'workspacetime.json'
SLEEP_TIME = 2
DISPLAY_FORMAT = 'Today: {}     Week: {}'


def increment_time():
    time_json = {}
    today = date.today().strftime("%d-%m-%Y")
    if os.path.isfile(TIME_FILE):
        with open(TIME_FILE, 'r') as file:
            time_json = json.load(file)

    time_json[today] = time_json.get(today, 0) + SLEEP_TIME
    with open(TIME_FILE, 'w') as file:
        json.dump(time_json, file, indent=4)

    show_total(time_json)


def show_total(time_json):
    today = date.today()
    dates = [today + timedelta(days=i)
             for i in range(0 - today.weekday(), 7 - today.weekday()) if i <= 0]

    total = 0
    for day in dates:
        total += time_json.get(day.strftime("%d-%m-%Y"), 0)

    display_str = DISPLAY_FORMAT.format(str(
        timedelta(seconds=time_json[today.strftime("%d-%m-%Y")])), str(timedelta(seconds=total)))

    print(display_str, end='\r')


def main():
    while True:
        if os.popen(WORKSPACE_CMD).read().strip() == '1':
            increment_time()
        sleep(SLEEP_TIME)


if __name__ == "__main__":
    main()
