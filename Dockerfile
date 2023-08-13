FROM python:latest

RUN mkdir -p /app
COPY ./web-server.py /app
WORKDIR /app

RUN pip install MarkupSafe==2.0.0
RUN pip install Flask

cmd ["python", "web-server.py"]]

