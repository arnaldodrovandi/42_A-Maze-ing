PYTHON = python3
MAIN_FILE = a_maze_ing.py
CONFIG_FILE = config.txt

.PHONY: install run debug clean lint lint-strict

install:
	$(PYTHON) -m pip install flake8 mypy pytest build

run:
	$(PYTHON) $(MAIN_FILE) $(CONFIG_FILE)

debug:
	$(PYTHON) -m pdb $(MAIN_FILE) $(CONFIG_FILE)

clean:
	find . -type d -name "__pycache__" -prune -exec rm -rf {} +
	rm -rf .mypy_cache .pytest_cache

lint:
	flake8 .
	mypy . --warn-return-any --warn-unused-ignores --ignore-missing-imports --disallow-untyped-defs --check-untyped-defs

lint-strict:
	flake8 .
	mypy . --strict
