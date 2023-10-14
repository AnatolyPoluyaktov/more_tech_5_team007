FROM python:3.11

ENV PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_CREATE=0 \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    DJANGO_SETTINGS_MODULE=sdl_platform.settings \
    PYTHONPATH=/code \
    REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt \
    PATH="${PATH}:/root/.local/bin"
WORKDIR /usr/src/app
RUN apt update && apt install -y gettext git curl postgresql-client
RUN curl -sSL https://install.python-poetry.org | python3 -
COPY pyproject.toml poetry.lock /code/
RUN poetry install --no-ansi


# copy entrypoint.sh
COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' /usr/src/app/entrypoint.sh
RUN chmod +x /usr/src/app/entrypoint.sh

COPY . /usr/src/app

ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
