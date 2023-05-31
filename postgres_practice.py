import psycopg2
import pandas as pd
import csv

#establishing the connection
conn = psycopg2.connect(
   database="mydb", user='postgres', password='12345678', host='127.0.0.1', port= '5432'
)
conn.autocommit = True

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

# #Preparing query to create a database
# sql = '''CREATE database IF NOT EXISTS mydb''';

# #Creating a database
# cursor.execute(sql)
# print("Database created successfully")

cursor.execute("CREATE TABLE IF NOT EXISTS employee(Name VARCHAR(40),designation VARCHAR(100), salary INT)")
print("Table created successfully")

# cursor.execute("INSERT INTO employee Values('Saifur Rahman','Data Analyst',20000)")
# cursor.execute("INSERT INTO employee Values('Rahul Paul','AI',30000)")
# print("Data Inserted Successfully")

cursor.execute("CREATE TABLE IF NOT EXISTS country(id SERIAL,province_state VARCHAR(100), country_region VARCHAR(100),lat VARCHAR(11),lon VARCHAR(11),date VARCHAR(40),confirmed INT,deats INT)")
print("Country Table created successfully")

cursor.execute(
    """CREATE TABLE IF NOT EXISTS corona(
    id SERIAL NOT NULL PRIMARY KEY,
    province_state VARCHAR(100),
    country VARCHAR(10),
    lat FLOAT,
    lon FLOAT,
    date DATE,
    confirmed INT,
    deaths INT
    )
    """)
with open("usa_county_wise.csv","r") as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        cursor.execute(
            "INSERT INTO corona VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",
            row
        )

# data = pd.read_csv("usa_county_wise.csv")
# df = pd.DataFrame(data)



# for row in df.itertuples():
#     #print(row)
#     cursor.execute('''
#                 INSERT INTO country (id, province_state, country_region,lat,lon,date,confirmed,deats)
#                 VALUES (?, ?, ?, ?, ?, ?, ?, ?)
#                 ''',
#                 (row.ID, 
#                 row.Province_State,
#                 row.Country_Region,
#                 row.LAT,
#                 row.LON,
#                 row.Date,
#                 row.Confirmed,
#                 row.Deaths
#                 )
#                 )


print("Data Inserted in corona Table Successfully")

#Closing the connection
conn.close()