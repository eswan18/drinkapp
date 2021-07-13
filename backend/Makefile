SRC_DIR = drinkapi
SRC_FILES = $(shell find $(SRC_DIR) -type f -name '*.py')
TEST_DIR = tests
TEST_FILES = $(shell find $(TEST_DIR) -type f -name '*.py')
SETUP_FILES = setup.cfg pyproject.toml

all: lint typecheck test

lint: $(SRC_FILES) $(TEST_FILES)
	flake8 $(SRC_DIR) $(TEST_DIR)

typecheck: $(SRC_FILES) $(TEST_FILES)
	mypy $(SRC_DIR) $(TEST_DIR)

test: $(SRC_FILES) $(TEST_FILES)
	pytest
