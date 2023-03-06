FROM python:latest

WORKDIR /app

COPY . .
COPY .env .
COPY requirements.txt .

RUN pip3 install -r requirements.txt

# Check if the  migrations directory exists
RUN if [ ! -d /app/migrations ]; then flask db init; fi

RUN flask db migrate && flask db upgrade

EXPOSE 5000

CMD ["flask", "run", "--host", "0.0.0.0"]

