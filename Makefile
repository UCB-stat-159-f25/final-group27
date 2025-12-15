BUILD_DIR=build

env:
	conda env create -f environment.yml || conda env update -f environment.yml

all:
	mkdir -p $(BUILD_DIR)
	jupyter nbconvert --to notebook --execute notebooks/data-cleanup.ipynb --output-dir $(BUILD_DIR)
	jupyter nbconvert --to notebook --execute notebooks/model_building.ipynb --output-dir $(BUILD_DIR)

test:
	pytest -q
