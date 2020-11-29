# Web

## Configure NGINX
* ./configure_nginx.sh

## Usage
##### First start
1) Run nginx: ./run_nginx.sh
2) Run server: ./run_server.sh

##### Reload
1) Stop server (Ctrl+C)
2) Reload nginx if needed: nginx -s reload 
3) Run server: ./run_server.sh

##### Stop server
1) Stop server (Ctrl+C)
2) Stop nginx: nging -s stop
