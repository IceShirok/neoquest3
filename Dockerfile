FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
COPY . /app
WORKDIR /app
RUN flask db init
RUN flask db migrate -m "users table"
RUN flask db upgrade
RUN python db_init.py
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["neoquest.py"]
