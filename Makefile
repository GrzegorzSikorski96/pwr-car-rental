bash:
	docker-compose exec python bash

up:
	docker-compose up -d

build:
	docker-compose build

down:
	docker-compose down -v

run: build start-mysql wait-for-database-connection up create-database

start-mysql:
	docker-compose up -d mysql

wait-for-database-connection:
	docker-compose run --rm python python3.9 manage.py wait_for_database_connection

create-database:
	docker-compose run --rm python python3.9 manage.py migrate

tests: build start-mysql wait-for-database-connection up
	docker-compose exec python mypy .
	docker-compose exec python python3.9 manage.py test
	docker-compose exec python flake8 --max-line-length 120 --exclude node_modules,migrations,venv
	docker-compose exec python bandit -r . --exclude /tests,./node_modules,/core/services/os_service.py,/venv
