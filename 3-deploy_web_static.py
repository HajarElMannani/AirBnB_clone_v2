#!/usr/bin/python3
'''Fabric script that creates and distributes an archive to your
web servers, using the function deploy'''
from fabric.api import local
from datetime import datetime
from fabric.api import put, run
from fabric.api import env
from os import path

env.hosts = ["54.236.45.210", "54.197.82.208"]
env.user = "ubuntu"
env.port = 22


def do_pack():
    '''generates a .tgz archive from the contents
    of the web_static folder'''
    time_now = datetime.now().strftime('%Y%m%d%H%M%S')
    archive_name = f"web_static_{time_now}.tgz"
    local('mkdir -p versions')
    res = local(f'tar -cvzf versions/{archive_name} web_static', capture=True)
    if res.failed:
        return None
    return f"versions/{archive_name}"


def do_deploy(archive_path):
    '''distributes an archive to your web servers,
    using the function do_deploy'''
    if (path.isfile(archive_path) is False):
        return False

    try:
        file_path = archive_path.split('/')[-1]
        file_extract = file_path.split('.')[0]
        extracted_file = "/data/web_static/releases/"
        if put(archive_path, "/tmp/").failed:
            return False
        if run(f"mkdir -p {extracted_file}{file_extract}").failed:
            return False
        if run(f"tar -xzf /tmp/{file_path} -C {extracted_file}{file_extract}").failed:
            return False
        if run(f"rm /tmp/{file_path}").failed:
            return False
        if run(f"mv {extracted_file}{file_extract}/web_static/* {extracted_file}{file_extract}/").failed:
            return False
        if run(f"rm -rf {extracted_file}{file_extract}/web_static").failed:
            return False
        if run("rm -rf /data/web_static/current").failed:
            return False
        if run(f"ln -s {extracted_file}{file_extract}/ /data/web_static/current").failed:
            return False

        print("New version deployed!")
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False


def deploy():
    '''reates and distributes an archive to your web servers'''
    arch_path = do_pack()
    if arch_path is None:
        return False
    return do_deploy(arch_path)
