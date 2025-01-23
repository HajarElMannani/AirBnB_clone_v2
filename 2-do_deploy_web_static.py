#!/usr/bin/python3
'''Fabric script (based on the file 1-pack_web_static.py) that distributes an archive to your web servers, using the function do_deploy'''
from fabric.api import put, run
from fabric.api import env
env.hosts = ['54.236.45.210', '54.197.82.208']


def do_deploy(archive_path):
    '''distributes an archive to your web servers,
    using the function do_deploy'''
    file_path = archive_path.split('/')[-1]
    try:
        put(f'{archive_path}', f'/tmp/{file_path}')
        extract_file = "data/web_static/releases/{}/".format(archive_path.rsplit('.')[0])
        run(f'mkdir -p /data/web_static/releases/{file_path}/')
        run(f'tar -xzf /tmp/{file_path} -C {extract_file}')
        run(f'rm  /tmp/{file_path}')
        run('rm -rf /data/web_static/current')
        run(f'ln -s {extract_file} /data/web_static/current')
    except Exception:
        return False
    return True
    
