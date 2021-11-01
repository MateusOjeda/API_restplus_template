FROM python:3.6

COPY requirements.txt /
RUN pip install --upgrade pip
RUN pip install -r /requirements.txt
COPY . /app
WORKDIR /app
EXPOSE 5003
