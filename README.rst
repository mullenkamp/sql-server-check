MSSQL server connection docker test
===================================

This repo and Dockerfile contains a simple app to test the docker connectivity to a MSSQL server attached to the network.
The parameters.yml needs to be filled out and can contain multiple tables per server and database.

To run the docker image, use the following example::

  docker run -v C:\path_to_yml\parameters.yml:/parameters.yml mullenkamp/sql-server-check

The parameters.yml file in this repo should be used as a template.
