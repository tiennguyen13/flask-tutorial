install:
	pip install -r requirements.txt

run:
	flask --app flaskr init-db
	flask --app flaskr run --debug

package:
	pip install -e .

test:
	pytest

coverage:
	coverage run -m pytest
	coverage report
	coverage html