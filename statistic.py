from config import USER_DB, PASSWORD_DB, HOST_DB, PORT_DB
import psycopg2
import server_info
import datetime
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


async def collect_statistic():
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
        sql_insert_data = f'insert into statistic (cpu_temp, ram, disk, date, time) ' \
                          f'values ({cpu_temp}, {ram}, {disk}, \'{date}\', \'{time}\')'
        cursor.execute(sql_insert_data)
    except (Exception, Error) as error:
        print(error)
    finally:
        if connection:
            cursor.close()
            connection.close()


def create_graph():
    now = datetime.datetime.now()
    date = now.strftime("%d/%m/%Y")
    cpu_temp_list = []
    date_list = []
    try:
        connection = psycopg2.connect(user=USER_DB,
                                      password=PASSWORD_DB,
                                      host=HOST_DB,
                                      port=PORT_DB,
                                      database='my_pi_server')
        connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cursor = connection.cursor()
        sql_select_data = f'select cpu_temp, time from statistic where date = \'{date}\';'
        cursor.execute(sql_select_data)
        rows = cursor.fetchall()
        for row in rows:
            cpu_temp_list.append(row[0])
            date_list.append(row[1])
        x = date_list
        y = cpu_temp_list
        plt.plot(x, y)
        plt.savefig('graph.png')
        image = Image.open('graph.png')
    except (Exception, Error) as error:
        print(error)
    finally:
        if connection:
            cursor.close()
            connection.close()
