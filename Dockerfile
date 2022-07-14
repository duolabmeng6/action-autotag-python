FROM python:3.10-slim-buster

ADD . /app
WORKDIR /app
RUN pip install --target=/app -r requirements.txt
RUN pip install --target=/app PyGithub
COPY main.py /app/main.py
ENV PYTHONPATH /app
CMD [ "python3", "main.py" ]

