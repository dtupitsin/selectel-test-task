FROM python:3.7-slim

WORKDIR /code

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

USER www-data:www-data
COPY app app

CMD ["gunicorn", "app:app", "-b", "0.0.0.0:8080", "-w", "4"]

