import psycopg2

from configparser import ConfigParser
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

from _functions._base_functions import create_table
from _functions.config import config


def popular_products():
    tablename = 'Popular_products'
    columns = '_id SERIAL NOT NULL, idproducts int NOT NULL, name VARCHAR(255) NULL, price DECIMAL NULL'

    create_table(tablename, columns)
