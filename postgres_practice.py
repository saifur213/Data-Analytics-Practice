import psycopg2

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

cursor.execute("CREATE TABLE employee(Name VARCHAR(40),designation VARCHAR(100), salary INT)")
print("Table created successfully")

cursor.execute("INSERT INTO employee Values('Saifur Rahman','Data Analyst',20000)")
cursor.execute("INSERT INTO employee Values('Rahul Paul','AI',30000)")
print("Data Inserted Successfully")

#Closing the connection
conn.close()