FROM python:3.7-slim

COPY Dockerfile requirements.txt sql_check.py ./

RUN apt-get update && apt-get install curl
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
RUN curl https://packages.microsoft.com/config/debian/10/prod.list > /etc/apt/sources.list.d/mssql-release.list
RUN ACCEPT_EULA=Y apt-get install -y unixodbc-dev msodbcsql17

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "sql_check.py", "parameters.yml"]
