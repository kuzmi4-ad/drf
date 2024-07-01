FROM python:3.11.4-alpine

ENV APP_HOME=/usr/src/app
WORKDIR /usr/src/app
RUN mkdir $APP_HOME/static

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY ./nginx.conf /etc/nginx/nginx.conf
COPY ./mime.types /etc/nginx/mime.types
COPY . .

ENTRYPOINT ["sh", "./entrypoint.sh"]



