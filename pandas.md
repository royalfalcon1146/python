### install pandas in cmd / terminal
`pip install pandas`
### highly recommended to plot graphs: install matplotlib module too
`pip install matplotlib`

---

### use pandas on a ready csv file then print it
```
myPandaTable = pandas.read_csv("csv file path")
print(myPandaTable)
```
### pandas can accept also dictionaries but they have to be written in the following way:
```
myDictionary = {
  "Companies":["BMW","Koenigsegg","Porsche"]
  "Cars":[20,9,40]
}

myPandaTable = pandas.DataFrame(myDictionary)
```

---

### If the csv or the data is pretty large, pandas will only print some of the rows and columns unless you set its options beforehand
```
pandas.options.display.max_rows=None
pandas.options.display.max_columns=None
```
### pandas might put some columns on another line unless you set the max line character width beforehand
```
pandas.options.display.width=1000
```

---

### Print Pandas table but sorted by a column in descending order
```
print(myPandaTable.sort_values(by="Column Name" ascending=False))
```
