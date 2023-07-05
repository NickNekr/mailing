
down-db:
	poetry run alembic downgrade base

up-db:
	poetry run alembic upgrade head

restart_db:
	make down-db
	make up-db


include .env
postgres:
	docker run --name pdb -e POSTGRES_PASSWORD=${DB_PASSWORD} -e POSTGRES_USER=${DB_USER} -e POSTGRES_DB=${DB_NAME} -e TZ=${DB_TIMEZONE} -d --rm -p${DB_PORT}:5432 postgres:latest

sending:
	poetry run python src/mailing/sending.py

tracking:
	poetry run python src/mailing/tracking.py

