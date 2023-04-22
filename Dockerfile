FROM python:alpine

WORKDIR /app

RUN python -m venv virtenv && pip install flask flask-bootstrap mysql-connector-python

COPY . .

EXPOSE 5000

CMD [ "flask", "run","--host","0.0.0.0","--port","5000"]