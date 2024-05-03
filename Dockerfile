FROM python:3.10.4

COPY requirements.txt .

RUN pip install -r requirements.txt

WORKDIR /app

COPY app.py .

COPY celerytask /app/celerytask/

EXPOSE 8000

CMD ["python", "app.py"]

#CMD ["tail", "-f", "/dev/null"]