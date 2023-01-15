install: #установка poetry
	poetry install

brain-games: #запуск brain-games 
	poetry run brain-games

build: 
	poetry build

publish: 
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

make lint: #запускаем flex8
	poetry run flake8 brain_games

	


