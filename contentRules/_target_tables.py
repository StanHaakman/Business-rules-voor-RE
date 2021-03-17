import psycopg2

from configparser import ConfigParser
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

from _functions._base_functions import create_table, get_data_query, store_data, empty_db_table, drop_table
from _functions.config import config


def target_tables():
    '''
    Business rule that add a table for every target audience. Per recommendation on the website 4 products are shown
    but for variation I choose to fill the different tables with 10 elements.

    :return:
    '''

    # First one is for Male products
    tablename = 'target_mannen'
    columns = "id SERIAL NOT NULL, idproducts VARCHAR(255) NOT NULL, name VARCHAR(255) NULL, price DECIMAL NULL, doelgroep VARCHAR(255) NULL"

    drop_table(tablename)
    create_table(tablename, columns)
    empty_db_table(tablename)

    data_query = "select idproducts, name, price, doelgroep from products WHERE doelgroep='Mannen' ORDER BY RANDOM() LIMIT 8;"

    data = get_data_query(data_query)

    store_query = f"insert into {tablename} (idproducts, name, price, doelgroep) values (%s, %s, %s, %s)"
    store_data(store_query, data)

    # Second one is for female products
    tablename = 'target_vrouwen'
    columns = "id SERIAL NOT NULL, idproducts VARCHAR(255) NOT NULL, name VARCHAR(255) NULL, price DECIMAL NULL, doelgroep VARCHAR(255) NULL"

    drop_table(tablename)
    create_table(tablename, columns)
    empty_db_table(tablename)

    data_query = "select idproducts, name, price, doelgroep from products WHERE doelgroep='Vrouwen' ORDER BY RANDOM() LIMIT 8;"

    data = get_data_query(data_query)

    store_query = f"insert into {tablename} (idproducts, name, price, doelgroep) values (%s, %s, %s, %s)"
    store_data(store_query, data)

    # Third one is for office products
    tablename = 'target_kantoor'
    columns = "id SERIAL NOT NULL, idproducts VARCHAR(255) NOT NULL, name VARCHAR(255) NULL, price DECIMAL NULL, doelgroep VARCHAR(255) NULL"

    drop_table(tablename)
    create_table(tablename, columns)
    empty_db_table(tablename)

    data_query = "select idproducts, name, price, doelgroep from products WHERE doelgroep='Kantoor' ORDER BY RANDOM() LIMIT 8;"

    data = get_data_query(data_query)

    store_query = f"insert into {tablename} (idproducts, name, price, doelgroep) values (%s, %s, %s, %s)"
    store_data(store_query, data)

    # Fourth one is for adult products
    tablename = 'target_volwassenen'
    columns = "id SERIAL NOT NULL, idproducts VARCHAR(255) NOT NULL, name VARCHAR(255) NULL, price DECIMAL NULL, doelgroep VARCHAR(255) NULL"

    drop_table(tablename)
    create_table(tablename, columns)
    empty_db_table(tablename)

    data_query = "select idproducts, name, price, doelgroep from products WHERE doelgroep='Volwassenen' ORDER BY RANDOM() LIMIT 8;"

    data = get_data_query(data_query)

    store_query = f"insert into {tablename} (idproducts, name, price, doelgroep) values (%s, %s, %s, %s)"
    store_data(store_query, data)

    # Fifth one is for child products
    tablename = 'target_kinderen'
    columns = "id SERIAL NOT NULL, idproducts VARCHAR(255) NOT NULL, name VARCHAR(255) NULL, price DECIMAL NULL, doelgroep VARCHAR(255) NULL"

    drop_table(tablename)
    create_table(tablename, columns)
    empty_db_table(tablename)

    data_query = "select idproducts, name, price, doelgroep from products WHERE doelgroep='Kinderen' ORDER BY RANDOM() LIMIT 8;"

    data = get_data_query(data_query)

    store_query = f"insert into {tablename} (idproducts, name, price, doelgroep) values (%s, %s, %s, %s)"
    store_data(store_query, data)
