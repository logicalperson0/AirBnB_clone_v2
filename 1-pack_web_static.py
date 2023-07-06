#!/usr/bin/python3
"""
Function that compress a folder
"""
"""
from fabric.api import local
from datetime import datetime
import os.path


def do_pack():
    try:
        if not os.path.exists("versions"):
            local("mkdir versions")

        format_time = datetime.now().strftime("%Y%m%d%H%M%S")
        f_name = 'versions/web_static_{}.tgz'.format(format_time)

        local("tar -cvzf {} web_static/".format(f_name))

        return f_name

    except Exception:
        return None
"""


from fabric.api import local
import time


def do_pack():
    """Generate an tgz archive from web_static folder"""
    try:
        local("mkdir -p versions")
        local("tar -cvzf versions/web_static_{}.tgz web_static/".
              format(time.strftime("%Y%m%d%H%M%S")))
        return ("versions/web_static_{}.tgz".format(time.
                                                    strftime("%Y%m%d%H%M%S")))
    except:
        return None
