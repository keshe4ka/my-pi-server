import os

# get cpu temperature
temperature = os.popen('vcgencmd measure_temp').readline()
# get Disk Space used %
# disk_space = os.popen("df -h /").read()
# get RAM info
# ram_info = os.popen('free').read()
# get uptime and cpu load average 1 min, 5min and 15 min
uptime = os.popen('uptime').readline()

info = temperature + '\n' + uptime
