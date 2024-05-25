FROM python:3.12-alpine

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

EXPOSE 8000

HEALTHCHECK --interval=15s --timeout=3s \
  CMD curl -f http://127.0.0.1:8000/ || exit 1

RUN --mount=type=cache,target=/root/.cache \
    pip install gunicorn

COPY requirements.txt .

RUN --mount=type=cache,target=/root/.cache \
    pip install -r requirements.txt

COPY src src

CMD gunicorn -b 0.0.0.0:8000 -k uvicorn.workers.UvicornWorker src.main:app