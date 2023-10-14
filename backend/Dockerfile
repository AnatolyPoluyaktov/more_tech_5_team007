FROM python:3.11.6-slim

ENV PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_CREATE=0 \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    DJANGO_SETTINGS_MODULE=src.settings \
    PYTHONPATH=/usr/src/app \
    PATH="${PATH}:/root/.local/bin"
WORKDIR /usr/src/app
RUN apt update && apt install -y gettext git curl postgresql-client
RUN curl -sSL https://install.python-poetry.org | python3 -
COPY pyproject.toml poetry.lock /usr/src/app/
RUN poetry install --no-ansi



COPY . .

#ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
