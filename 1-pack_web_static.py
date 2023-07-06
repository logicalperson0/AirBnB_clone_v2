#!/usr/bin/python3
"""
Function that compress a folder
"""
from fabric.api import local
from datetime import datetime
import os.path


def do_pack():
    """generates a .tgz archive from the contents of the web_static"""
    try:
        if not os.path.exists("versions"):
            local("mkdir versions")

        format_time = datetime.now().strftime("%Y%m%d%H%M%S")
        f_name = 'versions/web_static_{}.tgz'.format(format_time)

        local("tar -cvzf {} web_static".format(f_name))

        return f_name

    except Exception:
        return None
