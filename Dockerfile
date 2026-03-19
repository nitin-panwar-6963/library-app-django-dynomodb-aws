FROM python:3.11

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

WORKDIR /app/app

CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000"]
