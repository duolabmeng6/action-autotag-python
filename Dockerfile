FROM python:3-slim AS builder
ADD . /app
WORKDIR /app
RUN pip install --target=/app -r requirements.txt
RUN pip install --target=/app PyGithub

ENV PYTHONPATH /app
CMD ["/app/main.py"]