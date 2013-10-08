#Burbank Photo Gallery

## Requirements

* Python 2.7
* Pip
* Virtualenv
* Mongodb
* Sqlite3 for development, Postgresql for production

## Installation

* Clone repo
* virtualenv venv
* . venv/bin/activate
* pip install -r requirements.txt
* Put export.csv domain list in python folder
* cd python && python cache_json.py to cache json responses in mongo
* cd ../project
* python manage.py syncdb
* python manage.py to_sql to create django objects for studios/galleries/images

## Run

* cd project/
* python mange.py runserver 

