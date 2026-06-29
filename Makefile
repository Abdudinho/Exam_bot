mig:
	alembic revision --autogenerate -m "Create a baseline migrations"

head:
	alembic upgrade head

open_web:
	docker compose logs web -f

open_bot:
	docker compose logs bot -f
restart:
	docker compose restart

stop:
	docker compose stop

start:
	docker compose start

bot_migration:
	docker compose exec bot alembic revision --autogenerate -m "Create a baseline migrations"

bot_head:
	docker compose exec bot alembic upgrade head

down:
	docker compose down

up:
	docker compose up

rebuild:
	docker compose up --build

extract:
	pybabel extract --input-dirs=. -o locales/messages.pot

init:
	pybabel init -i locales/messages.pot -d locales -D messages -l en
	pybabel init -i locales/messages.pot -d locales -D messages -l uz
	pybabel init -i locales/messages.pot -d locales -D messages -l ru

compile:
	pybabel compile -d locales -D messages

update:
	pybabel update -d locales -D messages -i locales/messages.pot
