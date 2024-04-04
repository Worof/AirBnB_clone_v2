#!/usr/bin/python3
import os
from fabric.api import env, put, run

env.hosts = ['IP_web-01', 'IP_web-02']

def do_deploy(archive_path):
    if not os.path.exists(archive_path):
        return False
    # Upload the archive
    put(archive_path, '/tmp/')
    # Other commands to deploy
    # ...
    return True
