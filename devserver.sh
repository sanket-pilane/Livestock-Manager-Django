#!/bin/sh
source .venv/bin/activate
python livestock_manager/manage.py runserver $PORT
