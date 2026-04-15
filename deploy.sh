pip install -r requirements.txt

python manage.py migrate

python manage.py collectstatic --noinput

pkill gunicorn || true

gunicorn CSE3D.wgsi:application --bind 0.0.0.0:8000 --daemon