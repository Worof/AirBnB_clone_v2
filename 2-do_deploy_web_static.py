#!/usr/bin/python3
import os
from fabric.api import env, put, run

env.hosts = ['IP_web-01', 'IP_web-02']

def do_deploy(archive_path):
    if not os.path.isfile(archive_path):
        return False

    # Extract the file name from the archive path and prepare the base directory
    file_name = os.path.basename(archive_path)
    name = file_name.split(".")[0]
    dest = "/data/web_static/releases/" + name

    try:
        # Upload the archive
        put(archive_path, "/tmp/" + file_name)

        # Create directory where we will uncompress the archive
        run("mkdir -p {}".format(dest))

        # Uncompress the archive
        run("tar -xzf /tmp/{} -C {}".format(file_name, dest))

        # Remove the archive from the temporary folder
        run("rm /tmp/{}".format(file_name))

        # Move the contents out of the web_static folder to the parent folder
        run("mv {}/web_static/* {}".format(dest, dest))

        # Remove the empty web_static folder
        run("rm -rf {}/web_static".format(dest))

        # Delete the current symbolic link
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link pointing to the new release
        run("ln -s {} /data/web_static/current".format(dest))

        print("New version deployed!")
        return True
    except Exception as e:
        print(e)
        return False
