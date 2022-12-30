#!/home/bernandre07/.conda/envs/env/bin/python3
from csv_updater import thread
from database.models import coins
import os
from threading import Thread
import json


config = {
    'command_pallete': ">>>",
    'loggingLevel': 'info',
    'projectBaseDir': '/home/bernandre07/Desktop/dev/github-projects/AI/crypto-Ai/',
    'djangoDir': '',
    'scriptPath': os.getcwd(),
    'projectServices': {
        'webserver': 'web',
        'api': 'api',
    },
    'projectNetworks':{
        'frontend': 'frontendnet',
        'backend': 'backendnet',
    },
}


def begining():
    try:
        with open("dataShellConfig.json", "r") as file:
            global config
            config = json.load(file)
    except FileNotFoundError:
        print("Using default config")
    print("""
 _____________________________________________________
|     ____        __           _____ __         ____  |
|    / __ \____ _/ /_____ _   / ___// /_  ___  / / /  |
|   / / / / __ `/ __/ __ `/   \__ \/ __ \/ _ \/ / /   |
|  / /_/ / /_/ / /_/ /_/ /   ___/ / / / /  __/ / /    |
| /_____/\__,_/\__/\__,_/   /____/_/ /_/\___/_/_/     |
|_____________________________________________________|
        """)

def command_pallete(chars):
    execute(*input(f"{chars} ").split(' '))

def environment_setup():
    os.chdir(config['projectBaseDir'])
    if config['djangoDir'] == '':
        print("\033[0;31mWarning!\033[0m Please specify the django path or the script won't work properly")

def byee():
    print("\nByeee!")
    with open('dataShellConfig.json', 'w') as file:
        file.write(json.dumps(config))
    exit()



def manage_api(command):
    if command == 'up':
        os.system(f"docker-compose up -d api")
    if command == 'logs':
        os.system(f"docker-compose logs --tail=10 -f api")
    if command == 'stop' or command == 'down' or command == 'kill':
        os.system(f"docker-compose down")


def manage_web(command):
    if command == 'up':
        os.system(f"docker-compose up -d web")
    if command == 'logs':
        os.system(f"docker-compose logs --tail=10 -f web")
    if command == 'stop' or command == 'down' or command == 'kill':
        os.system(f"docker-compose down")


def csv_updater(coin):
    global csv_thread_command
    th = thread(coin, config['loggingLevel'])
    if csv_thread_command == 'start' or csv_thread_command == 'run':
        th.start()
    if csv_thread_command == 'kill' or csv_thread_command == 'stop' and th.status != 'Killed':
        th.kill()
    if csv_thread_command == 'status':
        print(th.config['status'])

def coin_main_thread():
    for coin in coins.current_coins():
        csv_updater(coin)

def execute(*args, **kwargs):
    if args[0] == 'shell':
        return os.system(" ".join(args[1:]))
    elif args[0] == 'clear':
        return os.system('clear')
    elif args[0] == 'set':
        config[args[1]] = " ".join(args[2:])
        return 0
    elif args[0] == 'show':
        if len(args) <= 1:
            return print("You need to specify more arguments.\nEX: show config")
        if args[1] == 'config':
            return print(json.dumps(config, indent=2))
    elif args[0] == 'updater':
        global csv_thread_command
        csv_thread_command = args[1]
        th = Thread(target=coin_main_thread)
        th.start()
    elif args[0] == 'api':
        manage_api(args[1])
    elif args[0] == 'web':
        manage_web(args[1])
    elif args[0] == 'services':
        print(config['projectServices'])
    elif args[0] == 'quit' or args[0] == 'exit':
        byee()
    else:
        print("Command not found!")
if __name__ == "__main__":
    begining()
    while True:
        try:
            command_pallete(config.get('command_pallete'))
        except KeyboardInterrupt:
            byee()
            break