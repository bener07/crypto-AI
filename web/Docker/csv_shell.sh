#!/home/bernandre07/.conda/envs/env/bin/python3
import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crypto_wallet.settings')
django.setup()
from csv_updater import run_csvs
from database.models import coins
import sys


config = {
    'command_pallete': ">>>",
    'loggingLevel': 'info',
}



def panel():
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

def execute(*args, **kwargs):
    if args[0] == 'shell':
        return os.system(" ".join(args[1:]))
    if args[0] == 'clear':
        return os.system('clear')
    if args[0] == 'set':
        config[args[1]] = " ".join(args[2:])
        return 0
    if args[0] == 'show':
        if len(args) <= 1:
            return print("You need to specify more arguments.\nEX: show config")
        if args[1] == 'config':
            return print(config)
    # if args[0] == 'run':
    #     if args[1] == 'updater':
    #         csvs(
    else:
        print("Command not found!")
if __name__ == "__main__":
    panel()
    while True:
        try:
            command_pallete(config.get('command_pallete'))
        except KeyboardInterrupt:
            print("\nByeee!")
            break