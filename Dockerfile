FROM python:3.10-slim-buster
ENV PYTHONPATH /app
ADD . /app
WORKDIR /app
RUN pip install --target=/app -r requirements.txt
RUN pip install --target=/app PyGithub
CMD [ "python3", "/app/main.py" ]

