FROM python:3.7-slim

COPY Dockerfile requirements.txt sql_check.py ./

RUN apt-get update && apt-get install -y unixodbc-dev gcc g++

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "sql_check.py", "parameters.yml"]
