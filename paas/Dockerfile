FROM ubuntu:20.04

RUN apt-get update -y && apt-get install -y python3-pip

WORKDIR /app

RUN pip3 install flask

RUN sed -i 's/basename(filename)/filename/' '/usr/local/lib/python3.8/dist-packages/werkzeug/debug/__init__.py'

COPY . /app

RUN gcc /app/flag.c -o /app/flag

RUN rm /app/flag.c

RUN chmod 111 flag

USER 1000:1000

ENTRYPOINT [ "python3" ]

CMD [ "pinasaservice.py" ]
