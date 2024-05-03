FROM python:3.10.4

COPY requirements.txt .

RUN pip install -r requirements.txt

WORKDIR /app
COPY celerytask
COPY tasks.py .
COPY call_task.py .

# Run app.py when the container launches
CMD ["celery", "-A", "tasks", "worker", "--loglevel=info"]