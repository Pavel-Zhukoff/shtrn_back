# цепляем рабочий образок
FROM python:alpine
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev jpeg-dev zlib-dev libjpeg
# Установили рабочую дирректорию образа
WORKDIR /usr/src/app
# скопировали из корня проекта в корень рабочей дирректории
COPY . .
# Установили переменные окружения:
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# устанавливаем зависимости
RUN pip install --upgrade pip
RUN pip install -r requirements.txt