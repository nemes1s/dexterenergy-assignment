#!/usr/bin/env python3
"""
Module Docstring
"""
from datetime import date

from entsoe import EntsoePandasClient
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
db_table = 'nl_de_flow'
api_key = '9e7b7f2f-1ac7-43a8-8d94-3e4ae89f0921'

# Connect to to the database
db_string = 'postgres://{}:{}@{}:{}/{}'.format(db_user, db_pass, db_host, db_port, db_name)
db = create_engine(db_string)

country_code_from = 'NL'
country_code_to = 'DE'
tz = 'Europe/Amsterdam'


def get_start_end():
    # sorry, never worked with sqlalchemy before
    result_set = db.execute('SELECT index from {} ORDER BY index DESC LIMIT 1'.format(db_table))
    result = [r[0] for r in result_set]
    if len(result):
        print(result[0])
        start = pd.Timestamp(result[0]).tz_convert(tz) + pd.Timedelta(seconds=1)
    else:
        start = pd.Timestamp(date.today(), tz=tz) - pd.Timedelta(days=365)  # yep this is ugly, i know

    end = start + pd.Timedelta(days=60)

    if end > pd.Timestamp(date.today(), tz=tz):
        end = pd.Timestamp(date.today(), tz=tz) + pd.Timedelta("23:59:59")
    return start, end


def main():
    client = EntsoePandasClient(api_key=api_key)
    (start, end) = get_start_end()

    response = client.query_crossborder_flows(country_code_from, country_code_to, start=start, end=end)
    response_revert_country_flow = client.query_crossborder_flows(country_code_to, country_code_from, start=start
                                                                  , end=end)
    # normalize
    result = response.to_frame() - response_revert_country_flow.to_frame()
    result.columns = ['value']
    if len(result):
        print(result.to_markdown())
        result.to_sql(db_table, db, if_exists='append')


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
