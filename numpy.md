# NumPy

## Installing and Importing

- Installing the module in the OS terminal
```
pip install numpy
```

- Importing the module in the code
```
import numpy
```

---

## Basics

- An Array in NumPy has a class type of **ndarray**

- Making a one, two, and three dimensional arrays respectively
```
myArray = numpy.array([1,2,3,4,5])
myArray = numpy.array([[1,2,3,4,5],[5,4,3,2,1]])
myArray = numpy.array([
  [[1,2,3,4,5],[5,9,2,7,8],[9,8,3,6,4]]
])
```

## Array Attributes
| Attribute | Description |
|-|-|
| ndarray.ndim | number of axes / dimensions of the array |
| ndarray.shape | this shows in detail how the array dimensions are shaped |
| ndarray.size | this gives the total number of elements in the array |
| ndarray.dtype | tells the type of elements in the array |
| ndarray.itemsize | the size in bytes of each element of the array |

## Array Creation

- Make an array full of zeros, made up of 2 lists with 4 zeros each
```
numpy.zeros((2,4))
```

- Make an array full of ones
```
numpy.ones((3,4))
```
