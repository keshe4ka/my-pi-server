from config import USER_DB, PASSWORD_DB, HOST_DB, PORT_DB
import psycopg2
import server_info
import datetime

from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


def collect_statistic():
    now = datetime.datetime.now()
    cpu_temp, ram, disk = server_info.to_statistic()
    date = now.strftime("%d/%m/%Y")
    time = now.strftime("%H:%M")
    try:
        connection = psycopg2.connect(user=USER_DB,
                                      password=PASSWORD_DB,
                                      host=HOST_DB,
                                      port=PORT_DB,
                                      database='my_pi_server')
        connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cursor = connection.cursor()
        sql_insert_data = f'insert into statistic (uptime, cpu_temp, ram, disk, date, time) ' \
                          f'values {cpu_temp}, {ram}, {disk}, {date}, {time}'
        cursor.execute(sql_insert_data)
    except (Exception, Error) as error:
        print(error)
    finally:
        if connection:
            cursor.close()
            connection.close()
