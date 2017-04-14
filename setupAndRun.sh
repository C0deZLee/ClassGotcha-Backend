#!/bin/bash

mkdir -p local
mkdir -p local/tmp

python manage.py makemigration
python manage.py migrate

python manage.py runserver
