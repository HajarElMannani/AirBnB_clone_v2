#!/usr/bin/python3
'''Fabric script (based on the file 1-pack_web_static.py) that distributes an archive to your web servers, using the function do_deploy'''
from fabric.api import put, run
from fabric.api import env


def do_deploy(archive_path):
    '''distributes an archive to your web servers,
    using the function do_deploy'''
    env.hosts = ['54.236.45.210', '54.197.82.208']
    try:
        put('$(archive_path)', '/tmp/')#/tmp/ of the server
        extract_file = "data/web_static/releases/{}".format(archive_path.rsplit('.')[0])
        run('tar -xzf $(archive_path) -C $(extract_file)')
        run('rm -r $(archive_path)')
        run('rm /data/web_static/current')
        run('ln -s /data/web_static/current $(extract_file)')
    except Exception:
        return False
    return True
    
