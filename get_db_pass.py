import boto3
import botocore.exceptions
import configparser
import json
import os
import pyperclip
from termcolor import colored


def get_base_dir():
    return os.path.dirname(os.path.abspath(__file__))


def get_aliases_from_file():
    filepath = os.path.join(get_base_dir(), 'aliases.json')
    with open(filepath, 'r') as f:
        return json.load(f)

def get_username():
    filepath = os.path.join(get_base_dir(), 'settings.ini')
    config = configparser.ConfigParser()
    config.read(filepath)
    if 'username' not in config['DEFAULT']: 
        username_input = input(colored('Please enter your username: ', 'magenta'))
        config['DEFAULT'] = {'username': username_input}
        with open(filepath, 'w') as configfile:
            config.write(configfile)
        return username_input
    return config['DEFAULT']['username']


def get_db_password_with_boto3(username, hostname, port, region, profile):
    session = boto3.Session(profile_name=profile)
    client = session.client('rds')
    password = client.generate_db_auth_token(DBHostname=hostname, Port=port, DBUsername=username, Region=region)
    return password


def main():
    try:
        username = get_username()
        alias_commands = get_aliases_from_file()

        for index, alias_command in enumerate(alias_commands, start=1):
            print(colored(f"{index}- {alias_command['name']}", 'yellow'))

        choice = input(colored("Please choose a number from the list: ", 'yellow'))
        selected_settings = alias_commands[int(choice) - 1]['command']
        password = get_db_password_with_boto3(username, **selected_settings)
        pyperclip.copy(password)
        print(colored("Password has been stored in the clipboard for security. You can access it by pasting (CTRL+V or CMD+V).", 'green'))

    except IndexError:
        print(colored('Error: Invalid choice. Please enter a number corresponding to the list of aliases.', 'red'))
    except FileNotFoundError:
        print(colored('Error: File not found. Make sure the aliases.json file exists.', 'red'))
    except json.decoder.JSONDecodeError:
        print(colored('Error: Unable to parse the aliases.json file. Check if the file is a valid JSON.', 'red'))
    except botocore.exceptions.ProfileNotFound:
        print(colored('Error: The provided boto3 profile could not be found. Make sure the profile is configured properly.', 'red'))
    except Exception as e:
        print(colored(f'An unexpected error occurred: {str(e)}', 'red'))

if __name__ == '__main__':
    main()
