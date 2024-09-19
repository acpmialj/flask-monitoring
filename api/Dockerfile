FROM python:3.7-alpine

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENV FLASK_APP /app/server.py

CMD flask --app /app/server.py run --host=0.0.0.0 --port=5000

EXPOSE 5000
