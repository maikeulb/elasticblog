#!/bin/sh
echo waiting for db
./wait-for-it.sh db:5432

flask db upgrade
flask seed-db

echo waiting for elasticsearch
./wait-for-it.sh elastic:9200 

echo executing gunicorn
exec gunicorn -b :5000 --access-logfile - --error-logfile - elasticblog:app
