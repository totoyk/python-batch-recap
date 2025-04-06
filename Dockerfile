FROM python:3.12

WORKDIR /app
COPY . /app
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

ENV PYTHONPATH=/app
# CMD ["python", "jobs/handlers/sample_handler.py"]