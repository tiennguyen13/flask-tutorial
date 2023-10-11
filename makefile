install:
	pip install -r requirements.txt

run:
	flask --app flaskr init-db
	flask --app flaskr run --debug