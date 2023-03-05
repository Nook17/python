import mysql.connector

try:
    # Ustawienia połączenia z bazą danych
    db = mysql.connector.connect(
      host="nazwa_hosta",
      user="nazwa_użytkownika",
      password="hasło_użytkownika",
      database="nazwa_bazy_danych"
    )
    
    # Tworzenie kursora
    cursor = db.cursor()

    # Zapytanie SQL
    sql = "SELECT * FROM tabela"

    # Wykonanie zapytania
    cursor.execute(sql)

    # Pobieranie wyników
    results = cursor.fetchall()

    # Wyświetlanie wyników
    for row in results:
      print(row)

    # Zamykanie połączenia
    db.close()

except mysql.connector.Error as error:
    print("Błąd przy próbie połączenia z bazą danych: {}".format(error))

