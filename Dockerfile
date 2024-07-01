FROM ubuntu:22.04

RUN apt-get update -y && \
    apt-get install -y python3-pip

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip3 install -r requirements.txt

COPY . /app

EXPOSE 3000

CMD ["flask", "--app", "phasebook", "add-dummy-data"]
CMD ["flask", "--app", "phasebook", "add-dummy-friend-request"]
CMD ["flask", "--app", "phasebook", "--debug", "run", "--host=0.0.0.0", "--port=3000"]
