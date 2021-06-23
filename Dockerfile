FROM python:3.8
MAINTAINER segev91.b@gmail.com
USER root
EXPOSE 8080
COPY * /
RUN pip3 install -r requirements.txt
ENV FLASK_APP=temperatureConverter.py
ENTRYPOINT ["/usr/local/bin/flask", "run", "--host=0.0.0.0", "--port=8080"]
