import os


# Получаем температуру процессора
def getCPUtemperature():
    res = os.popen('vcgencmd measure_temp').readline()
    return (res.replace("temp=", "").replace("'C\n", ""))


# Получаем загрузку процессора
def getCPUuse():
    return (str(os.popen("top -b -n1 | awk '/Cpu\(s\):/ {print $2}'").readline().strip( \
        )))


# Получаем информацию о дисковом пространстве
# Index 0: Объем диска
# Index 1: Занято на диске
# Index 2: Свободное место
# Index 3: Занято на диске в процентах
def getDiskSpace():
    p = os.popen("df -h /")
    i = 0
    while 1:
        i = i + 1
        line = p.readline()
        if i == 2:
            return (line.split()[1:5])


disk = getDiskSpace()
info = "[CPU_TEMP]: " + getCPUtemperature() + "\n[CPU_LOAD]: " + getCPUuse() + "\n[DISK]: " + disk[3]
