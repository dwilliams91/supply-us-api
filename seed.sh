#!/bin/bash
git rm -rf --cached db.sqlite3   
rm -rf rareapi/migrations
rm db.sqlite3
python3 manage.py migrate
python3 manage.py makemigrations supplyusapi
python3 manage.py migrate supplyusapi
python3 manage.py loaddata users
python3 manage.py loaddata tokens
python3 manage.py loaddata supplytypes
python3 manage.py loaddata supplyitems
python3 manage.py loaddata packagetypes
python3 manage.py loaddata classlists
python3 manage.py loaddata classlistsupplyitems
python3 manage.py loaddata userclasses
