# Цепляем рабочий образок
FROM python:3.8-alpine
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev jpeg-dev zlib-dev libjpeg libffi-dev make
# Установили рабочую дирректорию образа
WORKDIR /home/app
# Скопировали из корня проекта в корень рабочей дирректории
COPY ./app .
# Установили переменные окружения:
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# Устанавливаем зависимости
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8000

