FROM python:3.10-slim-buster
ENV PYTHONPATH /app
ADD . /app
WORKDIR /app
RUN pip install PyGithub
RUN pip install natsort
CMD [ "python3", "/app/main.py" ]

