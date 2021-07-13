FROM python:3.9.6-buster

EXPOSE 8000

COPY ./ /app/

WORKDIR /app

RUN pip install -e .

CMD uvicorn drinkapi.main:app --host 0.0.0.0
