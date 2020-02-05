FROM python:3.6

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY src src

CMD python3 -m src.server