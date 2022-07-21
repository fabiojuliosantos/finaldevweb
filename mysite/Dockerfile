FROM python:3.8.10
ENV PYTHONUNBUFFERED 1
WORKDIR /mysite
COPY requirements.txt /mysite
COPY . /mysite/
RUN pip install -r requirements.txt
WORKDIR  /mysite

CMD redis-server && python manage.py runserver 0.0.0.0:8000