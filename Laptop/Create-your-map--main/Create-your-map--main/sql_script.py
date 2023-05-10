import pymysql
import csv
import pandas as pd
import mysql.connector
# db = pymysql.connect("localhost","root","ELD880")
# Connect to SQL Server
db = mysql.connector.connect(host='localhost',
                      user='root',
                      password='ELD880',
                      database ='test13')

cursor = db.cursor()

# # Create Table
cursor.execute('DROP TABLE IF EXISTS test13.poi')
# cursor.execute('CREATE TABLE PM1 (fid int(11), name nvarcahr(100), lng decimal(10,7), lng float(10,6), category nvarchar(100))')
cursor.execute("CREATE TABLE IF NOT EXISTS test13.poi (fid int(11) NOT NULL DEFAULT '0', name varchar(100) NOT NULL DEFAULT '', lng decimal(10,7) DEFAULT NULL, lat float(10,6) DEFAULT NULL, category varchar(100) DEFAULT NULL)")


csv_data = csv.reader(open(r'C:\Users\mohit\OneDrive\Documents\IIOT-System-for-campus-mobility-system\Laptop\Create-your-map--main\Create-your-map--main\DATA.csv'))
next(csv_data)
for row in csv_data:
    cursor.execute('INSERT INTO test13.poi VALUES(%s, %s, %s, %s, %s)',row)

db.commit()
cursor.close()














# import pandas as pd
# import mysql.connector

# # Import CSV
# data = pd.read_csv (r'C:\Users\mohit\OneDrive\Documents\IIOT-System-for-campus-mobility-system\Laptop\Create-your-map--main\Create-your-map--main\DATA.csv')   
# df = pd.DataFrame(data, columns= ['Name','latitude','longitude','volt'])



# # Connect to SQL Server
# conn = mysql.connector.connect(host='localhost',
#                       user='root',
#                       password='ELD880',
#                       database="test5")
# cursor = conn.cursor()


# # Create Table
# cursor.execute('CREATE TABLE driver_info5 (Name nvarchar(50), latitude nvarchar(50), longitude nvarchar(50), volt nvarchar(50))')

# # Insert DataFrame to Table
# for row in df.itertuples():
#     cursor.execute('''
#                 INSERT INTO test5.dbo.driver_info5 (Name, latitude)
#                 VALUES (%s,%s)
#                 ''',
#                 str(row.Name), 
#                 str(row.latitude),
#                 )
#     cursor.execute('''
#                 INSERT INTO test5.dbo.driver_info4 (longitude, volt)
#                 VALUES (%s,%s)
#                 ''',
#                 row.longitude,
#                 row.volt
#                 )
#     print(row.Name)
# conn.commit()