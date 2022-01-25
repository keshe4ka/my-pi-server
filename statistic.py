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
    ram_list = []
    cpu_temp_list = []
    time_list = []
    try:
        connection = psycopg2.connect(user=USER_DB,
                                      password=PASSWORD_DB,
                                      host=HOST_DB,
                                      port=PORT_DB,
                                      database='my_pi_server')
        connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cursor = connection.cursor()
        sql_select_data = f'select ram, cpu_temp, time from statistic order by id desc limit 120;'
        cursor.execute(sql_select_data)

        rows = cursor.fetchall()
        for row in rows:
            ram_list.append(int(row[0]))
            cpu_temp_list.append(float(row[1]))
            time_list.append(str(row[2]))
        time_list.reverse()

        x = np.array(time_list)
        y = np.array(cpu_temp_list)
        plt.figure(figsize=(25, 5))
        plt.title("Температура CPU")
        plt.xlabel("время")
        plt.ylabel("температура, ℃")
        plt.grid()
        plt.xticks(rotation=90)
        plt.plot(x, y)
        plt.savefig('/home/pi/Documents/my_pi_server/photos/graph1.png')

        x = np.array(time_list)
        y = np.array(ram_list)
        plt.figure(figsize=(25, 5))
        plt.title("Использование RAM")
        plt.xlabel("время")
        plt.ylabel("память, MB")
        plt.grid()
        plt.xticks(rotation=90)
        plt.plot(x, y)
        plt.savefig('/home/pi/Documents/my_pi_server/photos/graph2.png')

    except (Exception, Error) as error:
        print(error)
    finally:
        if connection:
            cursor.close()
            connection.close()
