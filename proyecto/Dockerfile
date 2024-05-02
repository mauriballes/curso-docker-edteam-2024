FROM python:3.10.13-slim-bullseye

RUN apt-get update && \
    apt-get install libpq-dev -y

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY app.py app.py
CMD ["python", "app.py"]
