#!/usr/bin/python3
'''Fabric script (based on the file 1-pack_web_static.py) that distributes an archive to your web servers, using the function do_deploy'''
from fabric.api import put, run
from fabric.api import env
from os import path
env.hosts = ['54.236.45.210', '54.197.82.208']


def do_deploy(archive_path):
    '''distributes an archive to your web servers,
    using the function do_deploy'''
    if (path.isfile(archive_path) is False):
        return False
    file_path = archive_path.split('/')[-1]
    try:
        put(archive_path, f'/tmp/{file_path}')
        extract_file = "data/web_static/releases/{}/".format(archive_path.rsplit('.')[0])
        run(f'rm -rf {extract_file}/')
        run(f'mkdir -p {extract_file}/')
        run(f'tar -xzf /tmp/{file_path} -C {extract_file}')
        run(f'rm  /tmp/{file_path}')
        run(f'mv {extract_file}/web_static/* {extract_file}')
        run('rm -rf {extract_file}/web_static')
        run('rm -rf /data/web_static/current')
        run(f'ln -s {extract_file} /data/web_static/current')
    except Exception:
        return False
    return True
    
