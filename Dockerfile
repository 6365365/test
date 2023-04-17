FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /test

COPY requirements.txt /test
RUN pip install --upgrade pip -r requirements.txt

COPY ./ .

CMD uvicorn main:create_app --reload --host 0.0.0.0 --port 8000