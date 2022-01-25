# Телеграм-бот для отслеживания параметров вашей raspberryPi

<img align="center" width="414" height="641" src="https://github.com/keshe4ka/my_pi_server/blob/main/photos/Rz6oTi1Y5lk.jpg?raw=true">

### Как установить и настроить

1. Склонировать репозиторий
<br>
```git clone https://github.com/keshe4ka/my_pi_server.git```

2. Создать .env файл для хранения конфигов
<br>
```cd my_pi_server```
<br>
```nano .env```
<br>
Вставить переменные со значениями:
<br>
```BOT_TOKEN=12345
USER_DB=user
PASSWORD_DB=12345
HOST_DB=localhost
PORT_DB=5432
```

3. Установка пакетов
<br>
```pip3 install -r requirements.txt```

4. Установка и настройка supervisor 
<br>
```sudo apt update && sudo apt upgrade && sudo apt install supervisor```
<br>
```sudo nano /etc/supervisor/supervisord.conf```
<br>
В конец файла вставляем:
<br>
```[include]
files = /etc/supervisor/conf.d/*.conf```
<br>
```sudo nano /etc/supervisor/conf.d/my_pi_server```
<br>
Вставляем:
<br>
```[program:my_pi_server_bot]
command=/usr/bin/python3 указать_путь_к/bot.py
user=pi
process_name=%(program_name)s
numproc=4
autostart=1
autorestart=1
redirect_stderr=true
stderr_logfile=/var/log/my_pi_server_bot.err.log
stdout_logfile=/var/log/my_pi_server_bot.out.log
```
<br>
```sudo service supervisor start```
<br>
```sudo supervisorctl reread```
<br>
```sudo supervisorctl update```

5. Для построения графиков нужно создать БД
<br>
```sudo apt install postgresql```
<br>
```sudo su - postgres```
<br>
```psql```
<br>
```create user myuser with encrypted password 'mypass';```
<br>
```create database my_pi_server;```
<br>
```grant all privileges on database my_pi_server to myuser;```
<br>
```\c my_pi_server```
<br>
```CREATE TABLE statistic (
    id serial primary key,
    cpu_temp real,
    ram integer,
    disk real,
    date varchar(20),
    time varchar(20)
    varchar(80),
);```
<br>
```exit```

6. Запускаем
<br>
```sudo service supervisor start```

### Надеюсь, что вы не забыли про созданного с помощью @BotFather бота?
