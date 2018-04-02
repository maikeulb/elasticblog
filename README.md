# ElasticBlog

Mini Blog Engine that utilizes PostgreSQL and Elasticsearch (using
elasticsearch-py client) to index, query (full-text multi-match), and filter
through blog posts. 

Technology:
-----------
<hr>
* Flask
* PostgreSQL
* Elasticsearch
* Bulma

Run
---
If you have docker installed::
docker-compose build
docker-compose up
Go to http://localhost:5000

Otherwise, go to config.py and point the Postgresql and Elasticsearh variables so
that they point to your server URI's, set the FLASK_APP env variable to
elasticblog, and pip install the requirements. 

After all that has been taken care of::
flask db upgrade
flask seed-db
flask run
Go to http://localhost:5000
