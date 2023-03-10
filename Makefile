install: #установка poetry
	poetry install

brain-games: #запуск brain-games 
	poetry run brain-games

brain-even: #запуск brain-even
	poetry run brain-even

build: #cборка проекта
	poetry build

publish: #отладка проекта
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

make lint: #запускаем flex8
	poetry run flake8 brain_games

brain-calc: #запускаем brain-calc
	poetry run brain-calc

brain-gcd: #запускаем brain_gcd
	poetry run brain-gcd

brain-progression: #запускаем brain_progression
	poetry run brain-progression

brain-prime: #запускаем brain_prime
	poetry run brain-prime


