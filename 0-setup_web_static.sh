#!/usr/bin/env bash
#Script that sets up your web servers for the deployment of web_static.
sudo apt-get update -y
sudo apt-get install nginx -y
sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
sudo touch /data/web_static/releases/test/index.html
cat << EOF | sudo tee /data/web_static/releases/test/index.html
<!DOCTYPE html>
<html>
  <head>
  </head>
  <body>
ALX
  </body>
</html>
EOF
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R 'ubuntu':'ubuntu' /data/
cat <<EOF | sudo tee /etc/nginx/sites-available/default
server {
    listen 80 default_server;
    listen [::]:80 default_server;

    root /var/www/html;
    index index.html index.htm;
    add_header X-Served-By $(hostname);
    location = /data/web_static/current/ {
    	     alias /hbnb_static/;
	     index index.html index.htm;
    }
    location = /redirect_me {
        return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
    }

    error_page 404 /404.html;
    location = /404.html {
        internal;
        default_type text/html;
        return 404 "Ceci n'est pas une page";
    }
}
EOF
sudo service nginx restart
