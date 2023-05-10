import pandas as pd
import mysql.connector

# # Import CSV
# data = pd.read_csv (r'C:\Users\mohit\OneDrive\Documents\IIOT-System-for-campus-mobility-system\Laptop\Create-your-map--main\Create-your-map--main\DATA.csv')   
# df = pd.DataFrame(data, columns= ['Name','latitude','longitude','volt'])



# Connect to SQL Server
conn = mysql.connector.connect(host='localhost',
                      user='root',
                      password='ELD880')
cursor = conn.cursor()

#create database
cursor.execute("CREATE DATABASE test13")

cursor.execute("SHOW DATABASES")

for x in cursor:
  print(x)









# import mysql.connector

# try:
#     connection = mysql.connector.connect(host='localhost',
#                                          database='Electronics',
#                                          user='root',
#                                          password='ELD880')

#     mySql_Create_Table_Query = """CREATE TABLE Laptop ( 
#                              Id int(11) NOT NULL,
#                              Name varchar(250) NOT NULL,
#                              Price float NOT NULL,
#                              Purchase_date Date NOT NULL,
#                              PRIMARY KEY (Id)) """

#     cursor = connection.cursor()
#     result = cursor.execute(mySql_Create_Table_Query)
#     print("Laptop Table created successfully ")

# except mysql.connector.Error as error:
#     print("Failed to create table in MySQL: {}".format(error))
# finally:
#     if connection.is_connected():
#         cursor.close()
#         connection.close()
#         print("MySQL connection is closed")





# import mysql.connector

# try:
#     connection = mysql.connector.connect(host='localhost',
#                                          database='Electronics',
#                                          user='pynative',
#                                          password='pynative@#29')

#     mySql_insert_query = """INSERT INTO Laptop (Id, Name, Price, Purchase_date) 
#                            VALUES (%s, %s, %s, %s) """

#     records_to_insert = [(4, 'HP Pavilion Power', 1999, '2019-01-11'),
#                          (5, 'MSI WS75 9TL-496', 5799, '2019-02-27'),
#                          (6, 'Microsoft Surface', 2330, '2019-07-23')]

#     cursor = connection.cursor()
#     cursor.executemany(mySql_insert_query, records_to_insert)
#     connection.commit()
#     print(cursor.rowcount, "Record inserted successfully into Laptop table")

# except mysql.connector.Error as error:
#     print("Failed to insert record into MySQL table {}".format(error))

# finally:
#     if connection.is_connected():
#         cursor.close()
#         connection.close()
#         print("MySQL connection is closed")




