# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 15:59:37 2019

@author: MichaelEK
"""
import os
from pdsql import mssql
import pandas as pd
import pyodbc
import argparse
import yaml

# pd.options.display.max_columns = 10

##########################################
### Parameters

base_dir = os.path.realpath(os.path.dirname(__file__))

with open(os.path.join(base_dir, 'param.yml')) as param:
    param = yaml.safe_load(param)

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

        if 'col_names' in s:
            col_names = s['col_names']
        else:
            col_names = None

        sp1 = mssql.rd_sql(s['server'], s['database'], t, col_names, username=s['username'], password=s['password'])

        print(sp1.head())
    print('--Success')
