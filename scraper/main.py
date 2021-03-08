#!/usr/bin/env python3
"""
Module Docstring
"""
from datetime import date

from entsoe import EntsoePandasClient
from os import path
import pandas as pd
from sqlalchemy import create_engine

__author__ = "Dmytro Zadorozhnyi"
__version__ = "0.1.0"
__license__ = "MIT"

db_name = 'database'
db_user = 'username'
db_pass = 'secret'
db_host = 'db'
db_port = '5432'
api_key = '9e7b7f2f-1ac7-43a8-8d94-3e4ae89f0921'

# Connect to to the database
db_string = 'postgres://{}:{}@{}:{}/{}'.format(db_user, db_pass, db_host, db_port, db_name)
db = create_engine(db_string)

country_code_from = 'NL'
country_code_to = 'DE'
filename_to_store_end_date = 'lasttimestamp.txt'
tz = 'Europe/Amsterdam'


def get_start_end():
    if path.exists(filename_to_store_end_date):
        with open(filename_to_store_end_date, 'r') as file1:
            lasttimestamp = int(file1.readline())
            file1.close()
            start = pd.Timestamp(lasttimestamp, tz=tz) + pd.Timedelta("00:00:01")
    else:
        start = pd.Timestamp(date.today(), tz=tz) - pd.Timedelta("24:00:00")

    end = start + pd.Timedelta("24:00:00")
    return start, end


def write_end(end):
    with open(filename_to_store_end_date, "w") as file1:
        # Writing data to a file
        file1.write(str(end.value))
        file1.close()


def main():
    client = EntsoePandasClient(api_key=api_key)
    (start, end) = get_start_end()

    if end > pd.Timestamp(date.today(), tz=tz) + pd.Timedelta('24:00:00'):
        print("Nothing to add, date is greater than today")
        return

    response = client.query_crossborder_flows(country_code_from, country_code_to, start=start, end=end)
    response_revert_country_flow = client.query_crossborder_flows(country_code_to, country_code_from, start=start
                                                                  , end=end)
    # normalize
    result = response.to_frame() - response_revert_country_flow.to_frame()
    result.columns = ['value']
    print(result.to_markdown())
    # result.to_sql('nl_de_flow', db, if_exists='append')
    write_end(result.tail(1).index[0])


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
