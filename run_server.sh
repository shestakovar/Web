. env/bin/activate
python dish/manage.py collectstatic
cd dish
gunicorn --bind 0.0.0.0:8000 dish.wsgi &
DJANGO_SETTINGS_MODULE=dish.settings_read_only gunicorn --bind 0.0.0.0:8001 dish.wsgi &
DJANGO_SETTINGS_MODULE=dish.settings_read_only gunicorn --bind 0.0.0.0:8002 dish.wsgi &
while true ; do
	:
done
trap "kill $(jobs -p)" EXIT