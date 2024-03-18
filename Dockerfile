FROM python:3.9-slim-bookworm
USER root
RUN apt update && apt install curl git gcc make build-essential -y
COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt
COPY server.py /server.py
WORKDIR /
RUN chmod 777 /server.py
EXPOSE 7860
CMD uvicorn server:app --host 0.0.0.0 --port 7860
