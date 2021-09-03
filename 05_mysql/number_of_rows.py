# import required modules
import pymysql
# pymysql.install_as_MySQLdb()
import MySQLdb
  
# connect python with mysql with your hostname, 
# username, password and database
db= MySQLdb.connect("localhost", "root", "", "statement)
  
# get cursor object
cursor= db.cursor()
  
# get number of rows in a table and give your table
# name in the query
number_of_rows = cursor.execute("SELECT * FROM cfd_buy_calc")
  
# print the number of rows
print(number_of_rows)
