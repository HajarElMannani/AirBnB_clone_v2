#!/usr/bin/python3
'''Script that generates a .tgz archive from the contents
 of the web_static folder'''
from fabric.api import local
from datetime import datetime


def do_pack():
    '''generates a .tgz archive from the contents
    of the web_static folder'''
    time_now = datetime.now().strftime('%Y%m%d%H%M%S')
    archive_name = f"versions/web_static_{time_now}.tgz"
    local('mkdir -p versions')
    try:
        local(f'tar -cvzf {archive_name} web_static')
    except Exception:
        return None
    return archive_name
