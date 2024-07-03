- Installing the mysql connector library in the terminal 
```
pip install mysql-connector-python
```

---

- Connecting to the database
```
myDatabase = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "123456",
    database = "world"
)
```
- Making a cursor which is basically used to execute commands to the mysql database
```
myCursor = myDatabase.cursor()
```

---

- Execute a command then fetch it
```
myCursor.execute("command to execute here")
myCursorAnswer = myCursor.fetchall()
```
