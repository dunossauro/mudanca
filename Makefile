run:
	python run.py

check-lint:
	isort . --check-only
	blue . --check
	mypy .
