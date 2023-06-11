FROM python:latest

WORKDIR /usr/app/src

COPY udp.py xml/test.py xml/requirements.txt .

RUN pip install -r requirements.txt
CMD [ "python3", "test.py" ]
