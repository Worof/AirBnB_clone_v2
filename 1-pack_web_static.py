#!/usr/bin/python3
from fabric.api import local
from datetime import datetime

def do_pack():
    local("mkdir -p versions")
    file_name = "web_static_{}.tgz".format(datetime.strftime(datetime.now(), "%Y%m%d%H%M%S"))
    local("tar -cvzf versions/{} web_static".format(file_name))
    return "versions/{}".format(file_name)
