#!/usr/bin/env python3
# -*- coding: utf8 -*-
"""Alone-chat.py: Express yourself without hurting anyone"""

import os
from datetime import datetime

__author__ = "Tom Celestin"
__copyright__ = "Copyright 2018, Planet Earth"

def print_welcome():
    """Display welcome message."""
    os.system('clear')
    welcome = """
=================================================================================    
    Welcome to the

   mm   \"\"#                                  mmm  #               m
   ##     #     mmm   m mm    mmm          m\"   \" # mm    mmm   mm#mm
  #  #    #    #\" \"#  #\"  #  #\"  #         #      #\"  #  \"   #    #
  #mm#    #    #   #  #   #  #\"\"\"\"   \"\"\"   #      #   #  m\"\"\"#    #
 #    #   \"mm  \"#m#\"  #   #  \"#mm\"          \"mmm\" #   #  \"mm\"#    \"mm

    You can express yourself without hurting anyone
=================================================================================
    """
    print(welcome)


def ask_username():
    """Ask user's username."""
    username = input("Please enter your username: ")
    return username


def get_time():
    """Get current time formatted."""
    i = datetime.now()
    date_string = i.strftime('%H:%M:%S ')
    return date_string


def message_as(username):
    "Format prompt according to username."
    formatting = "[\033[94m" + username + "\033[0m] > " 
    if username == "system":
        formatting = "[\033[93msystem\033[0m] > "
    return get_time() + formatting


def system_message(username, joins):
    """Displays join and quit messages."""
    message = ""
    status = " \033[91mhas quit\033[0m"
    if joins:
        message += "\n"
        status =  " \033[92mhas joined\033[0m"
    message += message_as("system") + username + status
    print(message)


def save_logs(logs):
    """Save logs array in a file."""
    filename = get_time() + "alone-chat_logs.txt"
    file = open(filename,"w") 
    for message in logs:
        file.write(message+"\n") 
    file.close()


def read_command(command):
    """Return value depending on the command."""
    if command.startswith("/"):
        if command == "/help" or command == "/?":
            print(message_as("system") + "/export : Export messages from current conversation and quit")
            print(message_as("system") + "/help   : Display this help")
            print(message_as("system") + "/quit   : Quit Alone-Chat")
            return 0
        elif command == "/export":
            return 1
    else:
        return 0


def interface(username):
    """Display prompt and manage imputs."""
    system_message(username, True)
    formatted_username = message_as(username)
    message = ""
    logs = []
    while read_command(message) == 0:
        message = input(formatted_username)
        logs.append(message)
    if read_command(message) == 1:
        save_logs(logs)
    system_message(username, False)


def main():
    """The beginning of everything."""
    print_welcome()
    username = ask_username()
    interface(username)
    exit(1)

if __name__ == "__main__":
    main()
