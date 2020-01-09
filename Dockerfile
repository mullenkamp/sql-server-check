FROM python:3.7-buster

COPY Dockerfile requirements.txt sql_check_ConsentsReporting.py ./

# RUN apt-get update && apt-get install -y curl gnupg
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
RUN curl https://packages.microsoft.com/config/debian/10/prod.list > /etc/apt/sources.list.d/mssql-release.list
RUN apt-get update && ACCEPT_EULA=Y apt-get install -y unixodbc-dev msodbcsql17

RUN python3 -m pip install -r requirements.txt

CMD ["python", "sql_check_ConsentsReporting.py", "parameters.yml"]
