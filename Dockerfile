FROM python:3.12-slim

WORKDIR /app

COPY pyproject.toml .
COPY setup.py .
RUN pip install .

COPY src/ src/
CMD ["python", "-m", "src.main"]
