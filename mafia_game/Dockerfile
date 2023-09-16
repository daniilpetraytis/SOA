FROM python:3
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY . /code/

RUN pip install -r requirements.txt 

ENV PYTHONPATH /code

CMD [ "python", "/code/manage.py", "runserver", "0.0.0.0:8000"]
