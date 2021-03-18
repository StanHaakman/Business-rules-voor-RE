import psycopg2

from configparser import ConfigParser
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

from _functions._base_functions import create_table, get_data_query, store_data, empty_db_table, drop_table
from _functions.config import config


def preference_tables():
    '''
    Business rule to create table per session based on the preference. There will be 2 tables one for brand and one
    for category. There will be a session_id in the column and 4 product_ids.

    With that data u can use a join statement to get the data from sessions and products on the ids in the new tables
    :return:
    '''

    # First drop -> create -> empty table
    tablenames = [
        'preference_brand',
        'preference_category'
    ]

    tablequeries = [
        '_id serial not null, idsessions int not null, idproducts varchar not null, brand varchar null',
        '_id serial not null, idsessions int not null, idproducts varchar not null, category varchar null',
    ]

    for i, tablename in enumerate(tablenames):
        drop_table(tablename)
        create_table(tablename, columns=tablequeries[i])
        empty_db_table(tablename)
