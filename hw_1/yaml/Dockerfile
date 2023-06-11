FROM python:latest

WORKDIR /usr/app/src

COPY udp.py yaml/test.py yaml/requirements.txt .

RUN pip install -r requirements.txt
CMD [ "python3", "test.py" ]