#!/bin/bash

mkdir -p local
mkdir -p local/tmp

rm -rf *.pyc

python manage.py makemigrations
python manage.py migrate

python manage.py runserver
