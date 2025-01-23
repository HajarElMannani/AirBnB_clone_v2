#!/usr/bin/python3
'''Fabric script (based on the file 1-pack_web_static.py) that
 distributes an archive to your web servers, using the function
 do_deploy'''
from fabric.api import put, run
from fabric.api import env
from os import path
from fabric.api import local
from datetime import datetime
env.user = 'ubuntu'
env.hosts = ['54.236.45.210', '54.197.82.208']


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

def do_deploy(archive_path):
    '''distributes an archive to your web servers,
    using the function do_deploy'''
    if (path.isfile(archive_path) is False):
        return False
    try:
        file_path = archive_path.split('/', 1)[-1]
        file_extract = file_path.split('.', 1)[0]
        extracted_file = "/data/web_static/releases/{}/".format(file_extract)
        put(archive_path, "/tmp/{}".format(file_path))
        run("rm -rf {}".format(extracted_file))
        run("mkdir -p {}".format(extracted_file))
        run("tar -xzf /tmp/{} -C {}".format(file_path, extracted_file))
        run("rm  /tmp/{}".format(file_path))
        run("mv {}web_static/* {}".format(extracted_file, extracted_file))
        run("rm -rf {}web_static".format(extracted_file))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(extracted_file))
        print("New version deployed!")
    except Exception as e:
        print("Error: {}".format(e))
        return False
    return True
