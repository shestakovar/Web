FILENAME="dish/nginx.conf"
cp dish/nginx.conf.template $FILENAME

SEARCH="SITE_PATH"
REPLACE=$PWD
SEARCH2="NGINX_PATH"


if [[ "$OSTYPE" == "linux-gnu"* ]]; then
        REPLACE2="/etc/nginx"
        sed -i "s|$SEARCH|$REPLACE|g" "$FILENAME"
        sed -i "s|$SEARCH2|$REPLACE2|g" "$FILENAME"
elif [[ "$OSTYPE" == "darwin"* ]]; then
        REPLACE2="/usr/local/etc/nginx"
        sed -i "" "s|$SEARCH|$REPLACE|g" "$FILENAME"
        sed -i "" "s|$SEARCH2|$REPLACE2|g" "$FILENAME"
else
        echo "UNKNOWN OS. nginx_conf.sh"
fi
