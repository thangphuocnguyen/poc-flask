FROM python:3.5

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY . /usr/src/app

RUN chmod +x /usr/src/app/scripts/dj-run.sh

RUN pip install --no-cache-dir -r requirements/base.txt

ENV ENVIRONMENT=local
