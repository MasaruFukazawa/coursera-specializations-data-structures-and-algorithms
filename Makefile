SRC_DIR = coursera_specializations_data_structures_and_algorithms
TEST_DIR = tests

lint:
	python -m flake8 --ignore=E501 $(SRC_DIR)
	python -m flake8 --ignore=E501 $(TEST_DIR)
	python -m black $(SRC_DIR)
	python -m black $(TEST_DIR)
	python -m isort $(SRC_DIR)
	python -m isort $(TEST_DIR)
	python -m mypy --check-untyped-defs $(SRC_DIR)
	python -m mypy --check-untyped-defs $(TEST_DIR)

test:
	python -m pytest --cov=$(SRC_DIR) --cov-branch  --junitxml=pytest.xml --cov-report=term-missing:skip-covered | tee pytest-coverage.txt

prepare:
	make lint
	make test
