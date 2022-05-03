# Dockerfile for a Python App
FROM python:3.8
WORKDIR /rollover_api
COPY . .
RUN pip install -r requirements.txt
EXPOSE 5000
ENTRYPOINT ["python3", "app.py"]