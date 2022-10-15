FROM python:3.8
ENV PYTHONUNBUFFERED 1

ENV APP_PATH /var/www/app
RUN mkdir -p $APP_PATH

RUN apt-get update && apt-get -y install default-mysql-client
COPY requirements.txt $APP_PATH/
RUN pip install --upgrade pip && pip install -r $APP_PATH/requirements.txt

WORKDIR $APP_PATH
