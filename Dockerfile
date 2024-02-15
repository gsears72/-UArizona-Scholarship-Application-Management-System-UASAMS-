FROM python:3.10

ENV PYTHONBUFFERED=1

WORKDIR /code

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD python manage.py runserver 0.0.0.0:8000


