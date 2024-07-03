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
