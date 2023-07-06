#!/usr/bin/python3
"""
Fabric script based on the file 1-pack_web_static.py that distributes an
archive to the web servers
"""

from fabric.api import *
from datetime import datetime
import os
import shlex


env.hosts = ["54.85.96.179", "34.232.65.41"]

"""
def do_deploy(archive_path):
    distributes an archive to the web servers
    if not os.path.exists(archive_path):
        return False

    try:
        # put(archive_path, '/tmp/')
        name_arc = archive_path.split('/')[-1]
        no_tgz = name_arc.split('.')[0]
        pathing = '/data/web_static/releases/'

        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(pathing, no_tgz))
        run('tar -xzf /tmp/{} -C {}{}/'.format(name_arc, pathing, no_tgz))
        run('rm /tmp/{}'.format(name_arc))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(pathing, no_tgz))
        run('rm -rf {}{}/web_static'.format(pathing, no_tgz))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(pathing, no_tgz))

        print("New version deployed!")
        return True

    except Exception:
        return False
"""
def do_deploy(archive_path):
    """ Deploys """
    if not os.path.exists(archive_path):
        return False
    try:
        name = archive_path.replace('/', ' ')
        name = shlex.split(name)
        name = name[-1]

        wname = name.replace('.', ' ')
        wname = shlex.split(wname)
        wname = wname[0]

        releases_path = "/data/web_static/releases/{}/".format(wname)
        tmp_path = "/tmp/{}".format(name)

        put(archive_path, "/tmp/")
        run("mkdir -p {}".format(releases_path))
        run("tar -xzf {} -C {}".format(tmp_path, releases_path))
        run("rm {}".format(tmp_path))
        run("mv {}web_static/* {}".format(releases_path, releases_path))
        run("rm -rf {}web_static".format(releases_path))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(releases_path))
        print("New version deployed!")
        return True
    except:
        return False
