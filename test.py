import sqlite3
con = sqlite3.connect("employee_db.db")
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS employee(empName VARCHAR(40),empDesig VARCHAR(100), salary Numerical(11,2))")

cur.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='employee' ''')
if cur.fetchone()[0]==1 : {
	print('Employee Table exists.')
}

cur.execute("INSERT INTO employee Values('Saifur Rahman', 'Data Analyst',50000)")
cur.execute("INSERT INTO employee Values('Rahul Paul', 'Data Analyst',40000)")
res = cur.execute("SELECT * FROM employee")
print(res.fetchall())
