import sqlite3


connection = sqlite3.connect("student.db")

## cursor 
cursor = connection.cursor()

## create the table
table_info="""
Create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),
SECTION VARCHAR(25),MARKS INT);

"""

cursor.execute(table_info)

cursor.execute('''Insert Into STUDENT values('Shounak','Data Science','A',90)''')
cursor.execute('''Insert Into STUDENT values('Anurag','Data Science','B',100)''')
cursor.execute('''Insert Into STUDENT values('Sanjeev','Data Science','A',86)''')
cursor.execute('''Insert Into STUDENT values('Ritam','DEVOPS','A',50)''')
cursor.execute('''Insert Into STUDENT values('Dipesh','DEVOPS','A',35)''')

print("The inserted records are")
data=cursor.execute('''Select * from STUDENT''')
for row in data:
    print(row)

connection.commit()
connection.close()