# ElasticBlog

Mini blog engine that utilizes PostgreSQL and Elasticsearch (using
elasticsearch-py client) to index, query (full-text multi-match), and filter
through blog posts. 

Technology
----------
* Flask
* PostgreSQL
* Elasticsearch
* Bulma

Screenshots
---
### Post
![post](/screenshots/post.png?raw=true "Post")
### Index
Filter posts by category or tags, or perform a search.
![index](/screenshots/index.png?raw=true "Post")

Run
---
With docker:
```
docker-compose build
docker-compose up
Go to http://localhost:5000
```

Alternatively, create a database named 'elasticblog', open `config.py` and
point the PostgreSQL and Elasticsearch URIs to your servers, set the
`FLASK_APP` env variable to elasticblog.py, and install dependencies (e.g. `pip
install -r requirements.txt`). Be sure to install the
python dependencies using `requirements.txt` located in `./elasticblog/`, not
`./elasticblog/requirements/` (I'm working on pruning the dev/prod/test dependencies).


`cd` into `./elasticblog` (if you are not already); then run:
```
flask db upgrade
flask seed-db
flask run
Go to http://localhost:5000
```
