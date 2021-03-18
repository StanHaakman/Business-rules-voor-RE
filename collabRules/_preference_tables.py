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
        '_id serial not null, idsessions int not null, recommendation_one varchar not null, recommendation_two '
        'varchar not null,recommendation_three varchar not null, recommendation_four varchar not null, brand varchar '
        'null',

        '_id serial not null, idsessions int not null, recommendation_one varchar not null, recommendation_two '
        'varchar not null,recommendation_three varchar not null, recommendation_four varchar not null, '
        'category varchar null',
    ]

    for i, tablename in enumerate(tablenames):
        drop_table(tablename)
        create_table(tablename, columns=tablequeries[i])

        # Empty tables
        empty_db_table(tablename)

    # Idea to expand
    get_id_sessions_query = "select idsessions from sessions where preferences not like 'null';"
    idsessions = get_data_query(get_id_sessions_query)
    idsessions = [item for t in idsessions for item in t]

    idsessions = [2, 18, 32, 43, 45, 660]

    # Recieve requested data from database
    for current_session in idsessions:
        brandquery = f"select idsessions, preferences from sessions where preferences not like 'null' and idsessions={current_session};"

        data = get_data_query(brandquery)
        preference = data[0][1]
        preference = eval(preference)
        brand = preference.get('brand')
        brand = list(brand.keys())[0]
        category = preference.get('category')
        category = list(category.keys())[0]

        product_brand_query = f"select idproducts from products where brand='{brand}' order by RANDOM() limit 4;"
        product_brand_data = get_data_query(product_brand_query)
        product_brand_data.append((brand,))
        product_brand_data.insert(0, (data[0][0],))

        values = []
        for i in product_brand_data:
            values.append(i[0])
        values = tuple(values)

        # Store data in new database
        store_product_brand_query = f"insert into preference_brand (idsessions, recommendation_one, recommendation_two, recommendation_three, recommendation_four, brand) values (%s, %s, %s, %s, %s, %s);"
        store_data(store_product_brand_query, [values])

        product_category_query = f"select idproducts from products where category='{category}' order by RANDOM() limit 4;"
        product_category_data = get_data_query(product_category_query)
        product_category_data.append((category,))
        product_category_data.insert(0, (data[0][0],))

        values = []
        for i in product_category_data:
            values.append(i[0])
        values = tuple(values)

        store_product_category_query = f"insert into preference_category (idsessions, recommendation_one, recommendation_two, recommendation_three, recommendation_four, category) values (%s, %s, %s, %s, %s, %s);"
        store_data(store_product_category_query, [values])

