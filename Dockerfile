FROM python:3.8-alpine as pipenv
WORKDIR /requirements/
RUN pip install pipenv
COPY Pipfile* /
RUN pipenv lock --requirements > /requirements/base.txt
RUN pipenv lock --dev --requirements > /requirements/dev.txt

FROM python:3.8-alpine
RUN apk add \
    postgresql-dev \
    build-base \
    zlib-dev \
    libjpeg-turbo-dev
RUN mkdir /app
WORKDIR /app
COPY --from=0 /requirements .
RUN pip install -r base.txt

COPY . /app
