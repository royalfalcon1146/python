### install pandas in cmd / terminal
`pip install pandas`
### highly recommended to plot graphs: install matplotlib module too
`pip install matplotlib`

---

### use pandas on a ready csv file then print it
myPandaTable = pandas.read_csv("csv file path")
print(myPandaTable)

### pandas can accept also dictionaries but they have to be written in the following way:
`myDictionary = {
  "Companies":["BMW","Koenigsegg","Porsche"]
  "Cars":[20,9,40]
}

myPandaTable = pandas.DataFrame(myDictionary)`
