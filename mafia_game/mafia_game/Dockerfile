FROM python:3
ENV PYTHONUNBUFFERED 1
COPY ./requirements.txt /
COPY ./mafia_game /
RUN pip install -r requirements.txt
CMD python manage.py runserver