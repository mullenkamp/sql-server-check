# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 15:59:37 2019

@author: MichaelEK
"""
from pdsql import mssql
import pandas as pd
import pyodbc
import argparse
import yaml

pd.options.display.max_columns = 10

##########################################
### Parameters

parser = argparse.ArgumentParser()
parser.add_argument('yaml_path')
args = parser.parse_args()

with open(args.yaml_path) as param:
    param = yaml.safe_load(param)

##########################################
### tests

print(pyodbc.drivers())

for s in param:
    print('--Checking connectivity to server: ' + s['server'] + ' and database: ' + s['database'])
    for t in s['tables']:
        print('table: ' + t)

        sp1 = mssql.rd_sql(s['server'], s['database'], t, username=s['username'], password=s['password'])

        print(sp1.head())
    print('--Success')
