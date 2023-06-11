FROM python:latest

WORKDIR /usr/app/src

COPY udp.py message_pack/test.py message_pack/requirements.txt .

RUN pip install -r requirements.txt
CMD [ "python3", "test.py" ]
