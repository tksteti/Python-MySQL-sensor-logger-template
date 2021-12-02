import mysql.connector
import random
from datetime import datetime
import time

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="toor",
  database="testovac"
)

mycursor = mydb.cursor()

sql = "INSERT INTO logger (time, temper) VALUES (%s, %s)" #Základní insert příkaz -> NEMĚNÍ SE

while True:
    #generování hodnot
    temperka = random.randint(0,22)
    now = datetime.now()
    dt_string = now.strftime("%Y-%m-%d %H:%M:%S") #formátování času
    print(dt_string)

    #zapisování do databáze
    val = (temperka, dt_string) #hodnoty které budeme simulovat -> MĚNÍ SE
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")
    time.sleep(10)