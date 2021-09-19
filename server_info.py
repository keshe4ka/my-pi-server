import psutil
import time
import os
from config import intervals


# время прошедшее с момента загрузки системы в формате w:d:h:m
def get_uptime():
    seconds = time.time() - psutil.boot_time()
    result = []

    for name, count in intervals:
        value = int(seconds // count)
        if value:
            seconds -= value * count
            if value == 1:
                name = name.rstrip('s')
            result.append("{} {}".format(value, name))
    return ', '.join(result[:3])  # цифра 3 отвечает за отображение точности (до s/h/m...


# использование оперативной памяти
def get_ram_usage():
    usage = int((psutil.virtual_memory().total / 1024 - psutil.virtual_memory().available / 1024) / 1024)
    total = int(psutil.virtual_memory().total / 1024 / 1024)
    return str(usage) + " MiB / " + str(total) + " MiB"


# температура процессора
def get_cpu_temperature():
    res = os.popen("vcgencmd measure_temp").readline()
    return res.replace("temp=", "").replace("'C\n", "") + "℃"


# сколько занято на диске
def get_disk_usage():
    usage = int((psutil.disk_usage('/').total / 1024 - psutil.disk_usage('/').free / 1024) / 1024 / 1024)
    total = int(psutil.disk_usage('/').total / 1024 / 1024 / 1024)
    return str(usage) + " GiB / " + str(total) + " GiB" + "  (" + str(psutil.disk_usage('/').percent) + "%) "


# # Получаем загрузку процессора
# def getCPUuse():
#     return (str(os.popen("top -b -n1 | awk '/Cpu\(s\):/ {print $2}'").readline().strip( \
#         )))
#
#

# вывод всей информации
def get_info():
    return "[UPTIME]: " + get_uptime() \
           + "\n[CPU_TEMP]: " + get_cpu_temperature() \
           + "\n[RAM]: " + get_ram_usage() \
           + "\n[DISK]: " + get_disk_usage()
