VENV = venv
PYQA = $(VENV)/bin/pyqa
PYTHON = $(VENV)/bin/python3
PIP = $(VENV)/bin/pip
OS_PYTHON = python3
PYTEST = $(VENV)/bin/pytest


.PHONY: format
format:
	$(PYQA) format .

.PHONY: test
test:
	@echo "Running fast tests..."
	$(PYTEST) tests -vv -m "not slow"

.PHONY: test-a
test-a:
	@echo "Running all tests..."
	$(PYTEST) tests -vv

.PHONY: test-s
test-s:
	@echo "Running slow tests..."
	$(PYTEST) tests -vv -m "slow"

.PHONY: clean
clean:
	rm -f .coverage 2> /dev/null
	rm -rf dist 2> /dev/null
	rm -rf pyqa-report 2> /dev/null
	rm -rf .tox 2> /dev/null
	rm -rf mypy-precision 2> /dev/null
	rm -rf .mypy_cache 2> /dev/null
	rm -rf .pytest_cache 2> /dev/null
	rm -rf InfoCV.egg-info 2> /dev/null
	rm -rf logs 2> /dev/null
	rm -rf $(VENV) 2> /dev/null

.PHONY: build
build:
	$(PYTHON) setup.py install