
# running
run:
	python main.py

# CI checks
test-check:
	python -m pytest -v --no-header

bandit-check:
	bandit -r . -c "pyproject.toml"

format-check:
	black . --check

isort-check:
	isort --check .


# dev tasks
format:
	black .

isort:
	isort .

run-tests: test-check

check-linters: format-check isort-check

prepare-for-push: format isort

