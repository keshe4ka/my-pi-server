# Телеграм-бот для отслеживания параметров вашей raspberryPi

<img align="center" width="414" height="641" src="https://github.com/keshe4ka/my_pi_server/blob/main/photos/Rz6oTi1Y5lk.jpg?raw=true">

## Установка и настройка

### Склонировать репозиторий  
```git clone https://github.com/keshe4ka/my_pi_server.git```  

### Создать .env файл для хранения конфигов  
```cd my_pi_server```  

```nano .env```  

Вставить переменные со значениями:  
```
BOT_TOKEN=12345
USER_DB=user
PASSWORD_DB=12345
HOST_DB=localhost
PORT_DB=5432
```

### Установка пакетов  
```pip3 install -r requirements.txt```  

### Установка и настройка supervisor   
```sudo apt update && sudo apt upgrade && sudo apt install supervisor```  

```sudo nano /etc/supervisor/supervisord.conf```  

В конец файла вставляем:  
```
[include]
files = /etc/supervisor/conf.d/*.conf
```  

```sudo nano /etc/supervisor/conf.d/my_pi_server```    

Вставляем:  
```
[program:my_pi_server_bot]
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
```sudo service supervisor start```  

```sudo supervisorctl reread```  

```sudo supervisorctl update```  

### Для построения графиков нужно создать БД    
```sudo apt install postgresql```    

```sudo su - postgres```  

```psql```  

```create user myuser with encrypted password 'mypass';```  

```create database my_pi_server;```  

```grant all privileges on database my_pi_server to myuser;```  

```\c my_pi_server```  

```
CREATE TABLE statistic (
    id serial primary key,
    cpu_temp real,
    ram integer,
    disk real,
    date varchar(20),
    time varchar(20)
    varchar(80),
);
```  

```exit```

### Запускаем  
```sudo service supervisor start```

### Надеюсь, что вы не забыли про созданного с помощью @BotFather бота?
