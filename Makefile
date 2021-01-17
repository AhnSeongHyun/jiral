.PHONY: check format requirements

check:
	isort . --check-only
	black -S -l 110 --check jiral
	flake8

format:
	isort .
	black . --config pyproject.toml

requirements:
	pipenv run pip freeze > requirements.txt


