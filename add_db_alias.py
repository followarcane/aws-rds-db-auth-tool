import os
import json
from termcolor import colored

def get_alias_data_from_user():
    alias_name = input(colored('Enter alias name: ', 'magenta'))
    hostname = input(colored('Enter hostname: ', 'magenta'))
    port = input(colored('Enter port: ', 'magenta'))
    region = input(colored('Enter region: ', 'magenta'))
    profile = input(colored('Enter profile: ', 'magenta'))

    return {
        'name': alias_name,
        'command': {
            "hostname": hostname,
            "port": int(port),
            "region": region,
            "profile": profile
        }
    }

def add_alias_to_file(alias_data):
    if os.path.isfile('aliases.json'):
        with open('aliases.json', 'r') as f:
            content = f.read()
            aliases = json.loads(content) if content else []
    else:
        aliases = []

    aliases.append(alias_data)

    with open('aliases.json', 'w') as f:
        json.dump(aliases, f, indent=4)

def main():
    alias_data = get_alias_data_from_user()
    add_alias_to_file(alias_data)
    print(colored('Alias added successfully!', 'green'))

if __name__ == '__main__':
    main()
