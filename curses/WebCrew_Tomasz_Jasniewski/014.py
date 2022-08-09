# MySQL + python 3

# instalacja modułów ze strony MySQL
# https://dev.mysql.com/doc/connector-python/en/connector-python-installation-binary.html

# przykłady
# https://dev.mysql.com/doc/connector-python/en/connector-python-examples.html

# dokumentacja MySQLConnectionClass, MySQLCursor 
# https://dev.mysql.com/doc/connector-python/en/connector-python-api-mysqlconnection.html
# https://dev.mysql.com/doc/connector-python/en/connector-python-api-mysqlcursor.html

import mysql.connector
from mysql.connector import errorcode
import time

try:
  # odczyt
  mydb = mysql.connector.connect(host="localhost",user="user",passwd="1234",database="baza")
  cursor = mydb.cursor() # cursor - taki wskaźnik/uchwyt do poruszania się po bazie    
  query="SELECT id,ctime FROM actions WHERE id <= 40"  
  cursor.execute(query) # wykonujemy zapytanie SQL na obiekcie cursor
  for (id, ctime) in cursor:
    print("{}, {}".format(id,ctime));

  # wstawianie
  query="INSERT INTO cars2 SET regNr='IKSiGREK{}', descr='samochód teścia'".format(time.time())
  cursor.execute(query)
  lastid = cursor.lastrowid # ostatni dodany klucz
  mydb.commit() # zatwierdzenie faktycznej zmiany w tabeli/bazie

  # modyfikacja
  query="UPDATE cars SET descr='samochód teściowej' WHERE id={}".format(lastid)
  cursor.execute(query)
  mydb.commit()

  # pobieram ostatnio dodany car
  print("\n")
  query="SELECT regNr, descr FROM cars WHERE id={}".format(lastid)  
  cursor.execute(query) # wykonujemy zapytanie SQL na obiekcie cursor
  for (regNr,descr) in cursor:
    print("{}, {}\n\n".format(regNr,descr));

  # ciekawe, co to ? (nazwy kolumn i ilość wierszy objęta ostatnim zapytaniem)
  print(cursor.column_names, cursor.rowcount,'\n')   
  cursor.close()

  # tworzenie np. tabeli jest na takiej samej zasadzie...
  # ... po prostu wysyłamy odpowiednie zapytanie SQL
  
except mysql.connector.Error as err:
  print('Błąd przy połączeniu',err.errno,'\n',err)
except:
  print('Inny błąd','\n')
else:
  mydb.close()  
