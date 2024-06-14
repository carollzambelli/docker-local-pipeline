FROM python:3.9

RUN mkdir -p /usr/src

WORKDIR /usr/src

COPY . /usr/src

RUN pip install -r requirements.txt
RUN pip install mysql-connector-python
RUN pip install SQLAlchemy


