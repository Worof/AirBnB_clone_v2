#!/usr/bin/python3
from fabric.api import *

env.hosts = ['IP_web-01', 'IP_web-02']

def do_clean(number=0):
    number = int(number)

    # If number is 0 or 1, keep only the most recent archive
    if number == 0 or number == 1:
        number = 1
    else:
        number += 1  # Include the index offset

    # Local cleanup in the versions directory
    local('ls -tr versions/web_static_* | head -n -{} | xargs rm -rf'.format(number))

    # Remote cleanup in the /data/web_static/releases directory on each server
    for host in env.hosts:
        run('ls -tr /data/web_static/releases/web_static_* | head -n -{} | xargs rm -rf'.format(number))
