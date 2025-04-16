FROM python:3.11

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

CMD ["gunicorn", "app.main:app", "--bind=0.0.0.0:8000"]