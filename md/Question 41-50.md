# Question 41-50

## Question 41

> **_Write a program which can map() to make a list whose elements are square of elements in [1,2,3,4,5,6,7,8,9,10]._**  

---
My Solution

```python
def q41(s):
    return s**2
```

Result

```python
print(list(map(q41, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])))
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

## Question 42

> **_Write a program which can map() and filter() to make a list whose elements are square of even number in [1,2,3,4,5,6,7,8,9,10]._**  

---
My Solution

```python
def q42(lst):
    return list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, lst)))
```

Result

```python
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(q42(lst))
[4, 16, 36, 64, 100]
```

## Question 43

> **_Write a program which can filter() to make a list whose elements are even number between 1 and 20 (both included)._**  

---
My Solution

```python
def q43():
    return list(filter(lambda x: x % 2 == 0, range(1, 21)))
```

Result

```python
print(q43())
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
```

## Question 44

> **_Write a program which can map() to make a list whose elements are square of numbers between 1 and 20 (both included)._**  

---
My Solution

```python
def q44():
    return list(map(lambda x: x**2, range(1,21)))
```

Result

```python
print(q44())
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400]
```

## Question 45

> **_Define a class named American which has a static method called printNationality._**  
> **_You don't need self as param if static method is used_**  
---
My Solution

```python
class American():
    @staticmethod
    def printNationality():
        print("This is America.")
```

Result

```python
american = American()
american.printNationality()
This is America.
```

## Question 46

> **_Define a class named American and its subclass NewYorker._**  

---
My Solution

```python
class American():
    pass


class NewYorker(American):
    pass
```

Result

```python
american = American()
newyorker = NewYorker()
print(isinstance(newyorker, American))
True
```

## Question 47

> **_Define a class named Circle which can be constructed by a radius. The Circle class has a method which can compute the area._**  

---
My Solution

```python
class Circle():
    def __init__(self,r):
        self.radius = r

    def area(self):
        return 3.1416*(self.radius**2)
```

Result

```python
circle = Circle(5)
print(circle.area())
78.53999999999999
```

## Question 48

> **_Define a class named Rectangle which can be constructed by a length and width. The Rectangle class has a method which can compute the area._**  

---
My Solution

```python
class Rectangle ():
    def __init__(self, l, w):
        self.length = l
        self.width = w

    def area(self):
        return self.length*self.width
```

Result

```python
rectangle = Rectangle(10, 5)
print(rectangle.area())
50
```

## Question 49

> **_Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as argument. Both classes have a area function which can print the area of the shape where Shape's area is 0 by default._**  

---
My Solution

```python
class Shape():

    def area(self):
        return 0


class Square(Shape):
    def __init__(self, l=0):
        Shape.__init__(self)
        self.length = l

    def area(self):
        return self.length*self.length
```

Result

```python
square = Square(5)
print(square.area())
print(Square().area())
25
0
```

## Question 50

> **_Please raise a RuntimeError exception._**  

---
My Solution

```python
raise RuntimeError('something wrong')
```

Result

```python
Traceback (most recent call last):
  File "/mnt/c/python/break-the-ice-with-python/code/41-50.py", line 97, in <module>
    raise RuntimeError('something wrong')
RuntimeError: something wrong
```

[**Previous: Q31-40**](https://github.com/polo871209/break-the-ice-with-python/blob/main/md/Question%2031-40.md "Q31-40")  
[**Next: Q51-60**](https://github.com/polo871209/break-the-ice-with-python/blob/main/md/Question%2051-60.md "Q51-60")  
[**Home**](https://github.com/polo871209/break-the-ice-with-python "home")
