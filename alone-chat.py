#!/usr/bin/env python3
# -*- coding: utf8 -*-
"""Alone-chat.py: Express yourself without hurting anyone"""

import sys
from datetime import datetime

__author__ = "Tom Celestin"
__copyright__ = "Copyright 2018, Planet Earth"

def print_welcome():
    """Display welcome message."""
    welcome = """
    Welcome to the

   mm   \"\"#                                  mmm  #               m
   ##     #     mmm   m mm    mmm          m\"   \" # mm    mmm   mm#mm
  #  #    #    #\" \"#  #\"  #  #\"  #         #      #\"  #  \"   #    #
  #mm#    #    #   #  #   #  #\"\"\"\"   \"\"\"   #      #   #  m\"\"\"#    #
 #    #   \"mm  \"#m#\"  #   #  \"#mm\"          \"mmm\" #   #  \"mm\"#    \"mm

    You can express yourself without hurting anyone
    """
    print(welcome)


def ask_username():
    """Ask user's username."""
    username = input("Please enter your username: ")
    return username


def interface(username):
    """Display prompt and manage imputs."""
    formatted_username = "[\033[94m" + username + "\033[0m]"
    command = ""
    while command != "/quit" :
        i = datetime.now()
        date_string = i.strftime('%H:%M:%S ')
        command = input(date_string + formatted_username + " > ")
    print(username + " \033[91mhas quit")


def main():
    """The beginning of everything"""
    print_welcome()
    username = ask_username()
    interface(username)
    exit(1)

if __name__ == "__main__":
    main()
