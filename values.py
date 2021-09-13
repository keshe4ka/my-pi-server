import psutil
import time
import os
from config import intervals


# время прошедшее с момента загрузки системы в формате w:d:h:m
def get_uptime():
    seconds = time.time() - psutil.boot_time()
    result = []

    for name, count in intervals:
        value = seconds // count
        if value:
            seconds -= value * count
            if value == 1:
                name = name.rstrip('s')
            result.append("{} {}".format(value, name))
    return ', '.join(result[:4])


def get_ram_usage():
    usage = int((psutil.virtual_memory().total / 1024 - psutil.virtual_memory().available / 1024) / 1024)
    total = int(psutil.virtual_memory().total / 1024 / 1024)
    return str(usage) + " MiB / " + str(total) + " MiB"


def get_cpu_temperature():
    res = os.popen('vcgencmd measure_temp').readline()
    return res.replace("temp=", "").replace("'C\n", "")


# print(get_ram_usage())
# # Получаем температуру процессора
# def getCPUtemperature():
#     res = os.popen('vcgencmd measure_temp').readline()
#     return (res.replace("temp=", "").replace("'C\n", ""))
#
#
# # Получаем загрузку процессора
# def getCPUuse():
#     return (str(os.popen("top -b -n1 | awk '/Cpu\(s\):/ {print $2}'").readline().strip( \
#         )))
#
#
# # Получаем информацию о дисковом пространстве
# # Index 0: Объем диска
# # Index 1: Занято на диске
# # Index 2: Свободное место
# # Index 3: Занято на диске в процентах
# def getDiskSpace():
#     p = os.popen("df -h /")
#     i = 0
#     while 1:
#         i = i + 1
#         line = p.readline()
#         if i == 2:
#             return (line.split()[1:5])
#
#
# disk = getDiskSpace()
info = "[UPTIME]: " + get_uptime() \
       + "\n[CPU_TEMP]: " + get_cpu_temperature() \
       + "\n[RAM]: " + get_ram_usage()
#        + "\n[CPU_LOAD]: " + getCPUuse() \
#        + "\n[DISK]: " + disk[3]
