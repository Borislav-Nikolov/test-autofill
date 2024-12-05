FROM python:3.9

WORKDIR /app

COPY . .

RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install -U python-dotenv gevent Flask

EXPOSE 8080

CMD python -u ./main.py