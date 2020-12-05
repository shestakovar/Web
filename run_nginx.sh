mkdir -p logs
mkdir -p cache/temp
mkdir -p cache/logs
nginx -c `pwd`/dish/nginx.conf -p "`pwd`"
