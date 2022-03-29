
# running
run:
	python main.py

# CI checks
ci-tests:
	python -m pytest -v --no-header

ci-bandit-check:
	bandit -r . -c "pyproject.toml"

ci-black-check:
	black . --check

ci-isort-check:
	isort --check .

# Dev tasks (usually before pull requests)
format: ci-bandit-check
	black .
	isort .

test:
	python -m pytest -v --no-header

test-full-output:
	python -m pytest -v --no-header --capture=no

