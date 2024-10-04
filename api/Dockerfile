FROM python:3.7-alpine

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENV FLASK_APP /app/server.py

CMD python server.py

EXPOSE 5000
