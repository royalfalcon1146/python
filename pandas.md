- Install Pandas in the terminal
```
pip install pandas
```

- Installing Matplotlib for graphs too
```
pip install matplotlib
```

---

## Getting data and storing it in Pandas

- Use pandas on a ready csv file then print it
```
myPandaTable = pandas.read_csv("csv file path")
print(myPandaTable)
```

- Pandas can also accept dictionaries but they have to be written in the following way:
```
myDictionary = {
  "Companies":["BMW","Koenigsegg","Porsche"]
  "Cars":[20,9,40]
}

myPandaTable = pandas.DataFrame(myDictionary)
```

- Using Pandas with MySQL
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

- If the data is pretty large, pandas will only print some of the rows and columns unless you set its options beforehand
```
pandas.options.display.max_rows=None
pandas.options.display.max_columns=None
```

- Pandas might also put some columns on another line unless you set the max line character width beforehand
```
pandas.options.display.width=1000
```

---

## Common Functions with Pandas DataFrames

- Find all the column names in the table
```
print(myPandaTable.columns)
```

- Find the number of rows / records in the table
```
print(myPandaTable.index.stop)
```

- Print a certain row
```
print(myPandaTable.loc[RowNumberHere])
```

- Getting the value of a certain column from a row
```
print(myPandaTable.loc[RowNumberHere]["ColumnNameHere"])
```

- Print Pandas table but sorted by a column in descending order
```
print(myPandaTable.sort_values(by="Column Name" ascending=False))
```

- Print the first 10 rows from the Pandas table.
```
print(myPandaTable.head(10))
```

- Print the last 10 rows from the Pandas table.
```
print(myPandaTable.tail(10))
```

- After sorting too!
```
print(myPandaTable.sort_values(by="Column Name" ascending=False).head(10))
```

- Iterrating the rows in a dataframe and getting the value of a certain column
```
for row in myPandaTable.iterrows():
  row[1]["column_name"]
```

---

## Editing and Adding Data to DataFrames

- Editing a range of rows based on the indexes (0,10) at multiple columns (column1,column2) - This can be done with one row and one column
```
myPandaTable.loc[0:10,[column1,column2]] = [column1Value,column2Value]
```


---

## Plots and Graphs

- Plotting a graph, notice here that one of the columns should have **numerical data**, and the **graph type** could be one of the following: **line, bar, barh, kde, density, area, hist, box, pie, scatter, hexbin**
```
print(myPandaTable.plot("FirstColumnName","SecondColumnName",kind="graphType"))
```

- If you have a large data table, you could get the first 30 rows then plot them
```
print(myPandaTable.head(10).plot("Companies","Cars",kind="bar"))
```

- You could also do it after sorting
```
print(myPandaTable.sort_values(by="Cars", ascending=False).head(30).plot("Companies","Cars"))
```

- Naming the **x-axis and the y-axis labels** in the plot
```
print(myPandaTable.plot("Companies","Cars",kind="bar",xlabel="my x-axis",ylabel="my y-axis"))
```

- If you want to display a large figure with a lot of data, you could change the **figure size** and the **font size**
```
print(myPandaTabel.plot(figsize=(50,50),fontsize=10))
```
