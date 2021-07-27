all: uninstall clean docker_clean docker_build
clean_all: clean docker_clean

clean:
	@rm -rf .pytest_cache
	@rm -rf htmlcov
	@rm -f .coverage
	@rm -rf myapp.egg-info
	@find ./ -name "__pycache__" -exec rm -rf {} \; || true

install:
	pip install -e .['dev']

uninstall:
	pip uninstall myapp

docker_build:
	docker-compose up --build

docker_up:
	docker-compose up

docker_clean:
	docker-compose stop
	docker-compose rm -f
	docker rmi myapp_website || true
	docker rmi -f $(docker images -qf dangling=true) || true
