#!/usr/bin/python3
"""
Function that compress a folder
"""
from fabric.api import *


env.hosts = ["54.85.96.179", "34.232.65.41"]


def do_clean(number=0):
    """
    Deletes out-of-date archives, using the function do_clean
    """
    number = int(number)
    if number == 0:
        number = 2
    else:
        number += 1

    local('cd versions ; ls -t | tail -n +{} | xargs rm -rf'.format(number))
    pathing = '/data/web_static/releases'

    run('cd {} ; ls -t | tail -n +{} | xargs rm -rf'.format(path, number))
