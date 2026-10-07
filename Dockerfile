FROM python:3.12-slim

WORKDIR /app

RUN adduser app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

RUN chown app:app /app

COPY app.py .
USER app

EXPOSE 8080

CMD ["python", "app.py"]
