. env/bin/activate
python dish/manage.py collectstatic
cd dish
gunicorn --bind 0.0.0.0:8000 dish.wsgi
