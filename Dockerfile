FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential sqlite3
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
RUN mkdir /db
RUN /usr/bin/sqlite3 /app/app/app.db
ENTRYPOINT ["python"]
CMD ["neoquest.py"]
