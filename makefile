help: ## help
	@egrep -h '\s##\s' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

build: stop ## build services
	docker-compose build

up: stop ## run services
	docker-compose up

upd: stop ## run services in background
	docker-compose up -d

clean: ## stop all services
	docker-compose down --remove-orphans

stop: ## stop all services
	docker-compose stop

rebuild: ## rebuild and run services from scratch
	docker-compose up --build -d

migrate: ## run migrations; could be issues with starting bd
	python transport_api/manage.py makemigrations && python transport_api/manage.py migrate