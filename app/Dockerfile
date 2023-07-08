FROM python:3.11-slim as requirements-stage

WORKDIR /tmp

# install system dependencies
RUN apt-get update && python -m venv /opt/venv

# Make sure we use the virtualenv:
ENV PATH="/opt/venv/bin:$PATH"

# install python dependencies
COPY ./requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

FROM python:3.11-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

COPY --from=requirements-stage /opt/venv /opt/venv

# Make sure we use the virtualenv:
ENV PATH="/opt/venv/bin:$PATH"

COPY . .

ENTRYPOINT uvicorn api.server:app --reload --host 0.0.0.0 --port "$SERVER_PORT"
