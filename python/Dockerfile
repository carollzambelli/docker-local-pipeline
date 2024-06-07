FROM python:3.9

RUN mkdir -p /usr/src/python

WORKDIR /usr/src/python

COPY . /usr/src/python

RUN pip install -r requirements.txt
RUN pip install mysql-connector-python
RUN pip install SQLAlchemy