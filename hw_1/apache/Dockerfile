FROM python:latest

WORKDIR /usr/app/src

COPY udp.py apache/test.py apache/requirements.txt .

RUN pip install -r requirements.txt
CMD [ "python3", "test.py" ]
