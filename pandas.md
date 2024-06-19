Install Pandas in the terminal
```
pip install pandas
```
Installing Matplotlib for graphs too
```
pip install matplotlib
```

---

## Getting data and storing it in Pandas

Use pandas on a ready csv file then print it
```
myPandaTable = pandas.read_csv("csv file path")
print(myPandaTable)
```
Pandas can also accept dictionaries but they have to be written in the following way:
```
myDictionary = {
  "Companies":["BMW","Koenigsegg","Porsche"]
  "Cars":[20,9,40]
}

myPandaTable = pandas.DataFrame(myDictionary)
```
Using Pandas with MySQL
```
myDictionary={}

Cursor.execute("show columns from tablename")
columns = Cursor.fetchall()

Cursor.execute("select * from tablename")
tablename = Cursor.fetchall()

for number,column in enumerate(columns):
  myDictionary[column[0]]=[] 
  for row in tablename:
      try:
          myDictionary[column[0]].append(int(row[number]))
      except:
          myDictionary[column[0]].append(row[number])

myPandaTable = pandas.DataFrame(myDictionary)
```

---
## Common Problems

If the data is pretty large, pandas will only print some of the rows and columns unless you set its options beforehand
```
pandas.options.display.max_rows=None
pandas.options.display.max_columns=None
```
Pandas might also put some columns on another line unless you set the max line character width beforehand
```
pandas.options.display.width=1000
```

---

Find all the column names in the table
```
print(myPandaTable.columns)
```
Find the number of rows / records in the table
```
print(myPandaTable.count())
```
Print Pandas table but sorted by a column in descending order
```
print(myPandaTable.sort_values(by="Column Name" ascending=False))
```
Print the first 10 rows from the Pandas table.
```
print(myPandaTable.head(10))
```
Print the last 10 rows from the Pandas table.
```
print(myPandaTable.tail(10))
```
After sorting too!
```
print(myPandaTable.sort_values(by="Column Name" ascending=False).head(10))
```
