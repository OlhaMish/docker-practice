FROM python:3.10-bookworm

WORKDIR /app

COPY requirements.txt .

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["uvicorn", "spaceship.main:app", "--host=0.0.0.0", "--port=8080"]
