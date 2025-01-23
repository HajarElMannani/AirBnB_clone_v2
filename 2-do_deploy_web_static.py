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
    try:
        file_path = archive_path.split('/')[-1]
        put(archive_path, f'/tmp/{file_path}')
        file_extract = file_path.split('.')[0]
        extracted_file = "data/web_static/releases/{}/".format(file_extract)
        run(f'rm -rf {extracted_file}/')
        run(f'mkdir -p {extracted_file}/')
        run(f'tar -xzf /tmp/{file_path} -C {extracted_file}')
        run(f'rm  /tmp/{file_path}')
        run(f'mv {extracted_file}web_static/* {extracted_file}')
        run(f'rm -rf {extracted_file}web_static')
        run('rm -rf /data/web_static/current')
        run(f'ln -s {extracted_file} /data/web_static/current')
    except Exception:
        return False
    return True
    
