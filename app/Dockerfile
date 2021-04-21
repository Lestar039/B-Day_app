FROM python:3.8-alpine

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# RUN apt-get install python3-pip python3-dev libpq-dev postgresql postgresql-contrib

# set work directory
RUN mkdir -p /user/src/app/
WORKDIR /user/src/app/

COPY . /user/src/app/

# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

RUN pip install --upgrade pip
#RUN pip install psycopg2-binary
RUN pip install --no-cache-dir -r requirements.txt

#RUN \
# apk add --no-cache python3 postgresql-libs && \
# apk add --no-cache --virtual .build-deps gcc python3-dev musl-dev postgresql-dev && \
# python3 -m pip install -r requirements.txt --no-cache-dir && \
# apk --purge del .build-deps

