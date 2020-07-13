FROM python:3.7.6-buster as server


WORKDIR /server
COPY triof_app.py /server/
COPY requirements.txt /server
COPY templates /server/templates
COPY static /server/static
COPY src /server/src
COPY camera /server/camera

RUN pip3 install -r /server/requirements.txt

EXPOSE 8080

CMD python3 ./triof_app.py
