import os
from time import sleep

WORKSPACE_CMD = "wmctrl -d | grep '*' | cut -d ' ' -f1"
TIME_FILE = 'workspacetime.txt'
SLEEP_TIME = 2

def increment_time():
    time = '1'
    if os.path.isfile(TIME_FILE):
        with open(TIME_FILE, 'r') as file:
            time = file.readline().strip()

    time_int = int(time) + SLEEP_TIME
    with open(TIME_FILE, 'w') as file:
        file.write(str(time_int)+'\n')
    
def main():
    while True:
        if os.popen(WORKSPACE_CMD).read().strip() == '1':
            increment_time()
        sleep(SLEEP_TIME)

if __name__ == "__main__":
   main()