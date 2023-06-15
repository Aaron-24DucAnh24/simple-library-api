FROM python:3.9-bullseye
COPY database/ /app/database
COPY src/ /app/src
COPY ./requirements.txt /app
COPY ./.env /app
WORKDIR /app
RUN python3 -m pip install -r requirements.txt
CMD flask --app src/app run --host=0.0.0.0 --port=5000