# Zapisovač hodnot do databáze - python template

Jednoduchá aplikace na zapisovaní hodnot do tabulky

update programu ve složce s gitem **git fetch** 


## Instalace LAMP

sudo apt update -y && sudo apt upgrade -y

sudo apt install apache2 -y

sudo apt install php -y

sudo nano /var/www/html/test.php 

sudo apt install mariadb-server php-mysql -y

sudo mysql_secure_installation

sudo mysql -uroot -p
grant all privileges on *.* to 'phpmyadmin'@'localhost';
flush privileges;
quit


## Instalace knihoven
pip install mysql-connector-python
pip install gpiozero
