install:
	pip install --upgrade pip &&\
	pip install -r requirements.txt

format:
	black *.py
	
lint:
	pylint --disable=R,C consola_calculo.py
	pylint --disable=R,C calculadora_indices.py
	
test:
	python -m pytest -vv --cov=sequences_calculator test_code.py

all: install lint format test