run:
	uv run -m src.main

install:
	uv pip install -e .

venv:
	uv venv
