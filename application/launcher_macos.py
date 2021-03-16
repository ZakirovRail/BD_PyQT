# for MacOs version of launcher
from subprocess import Popen
import os
import time

process = []
PATH_TO_FILE = os.path.dirname(__file__)
PATH_TO_SCRIPT_SERVER = os.path.join(PATH_TO_FILE, "server.py")
PATH_TO_SCRIPT_CLIENTS = os.path.join(PATH_TO_FILE, "client.py")

while True:
    action = input("Select an action: q - quite, s - run server and client, x - close all applications: ")

    if action == 'q':
        break
    elif action == 's':
        process.append(Popen(['python3', f'{PATH_TO_SCRIPT_SERVER}'], shell=True))
        process.append(Popen(['python3', f'{PATH_TO_SCRIPT_CLIENTS}', '-n', 'test1'], shell=True))
        time.sleep(0.5)
        process.append(Popen(['python3', f'{PATH_TO_SCRIPT_CLIENTS}', '-n', 'test2'], shell=True))
        time.sleep(0.5)
        process.append(Popen(['python3', f'{PATH_TO_SCRIPT_CLIENTS}', '-n', 'test3'], shell=True))
    elif action == 'x':
        while process:
            victim = process.pop()
            victim.kill()
