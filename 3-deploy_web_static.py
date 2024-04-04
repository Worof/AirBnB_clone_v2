#!/usr/bin/python3
from fabric.api import local, put, run, env
import os
from datetime import datetime

env.hosts = ['IP_web-01', 'IP_web-02']
env.user = 'ubuntu'
# If you're using SSH keys for authentication, specify the path to your private key
# For example: env.key_filename = '/path/to/private/key'

def do_pack():
    """Generates a .tgz archive from the contents of the web_static folder"""
    try:
        local("mkdir -p versions")
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        archive_path = "versions/web_static_{}.tgz".format(timestamp)
        local("tar -cvzf {} web_static".format(archive_path))
        return archive_path
    except:
        return None

def do_deploy(archive_path):
    """Distributes an archive to web servers"""
    if not os.path.exists(archive_path):
        return False
    try:
        file_name = os.path.basename(archive_path)
        name = file_name.split(".")[0]
        remote_path = "/tmp/{}".format(file_name)
        put(archive_path, remote_path)
        run("mkdir -p /data/web_static/releases/{}/".format(name))
        run("tar -xzf {} -C /data/web_static/releases/{}/".format(remote_path, name))
        run("rm {}".format(remote_path))
        run("mv /data/web_static/releases/{}/web_static/* /data/web_static/releases/{}/".format(name, name))
        run("rm -rf /data/web_static/releases/{}/web_static".format(name))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{}/ /data/web_static/current".format(name))
        return True
    except:
        return False

def deploy():
    """Creates and distributes an archive to web servers"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
