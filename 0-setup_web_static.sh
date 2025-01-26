#!/usr/bin/env bash
#Script that sets up your web servers for the deployment of web_static
sudo apt-get update -y
sudo apt-get install nginx -y
sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
sudo touch /data/web_static/releases/test/index.html
cat << 'EOF' | sudo tee /data/web_static/releases/test/index.html
<html>
  <head>
  </head>
  <body>
ALX
  </body>
</html>
EOF

sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i '/listen 80 default_server/a location /hbnb_static { alias /data/web_static/current/;}' /etc/nginx/sites-enabled/default
sudo service nginx restart
