#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate

# ESTA LÍNEA CARGARÁ TUS DATOS:
python manage.py loaddata data_dump.json
