# Question 81-90

## Question 81

> **_By using list comprehension, please write a program to print the list after removing numbers which are divisible by 5 and 7 in [12,24,35,70,88,120,155]._**  

---
My Solution

```python
li = [12,24,35,70,88,120,155]
li = [x for x in li if x % 35!=0]
print(li)
```

Result

```python
[12, 24, 88, 120, 155]
```

## Question 82

> **_By using list comprehension, please write a program to print the list after removing the 0th, 2nd, 4th,6th numbers in [12,24,35,70,88,120,155]._**  

---
My Solution

```python
li = [12,24,35,70,88,120,155]
li = [li[i] for i in range(len(li)) if i%2 != 0 and i <= 6]
print(li)
```

Result

```python
[24, 70, 120]
```

## Question 83

> **_By using list comprehension, please write a program to print the list after removing the 2nd - 4th numbers in [12,24,35,70,88,120,155]_**  

---
My Solution

```python
li = [12, 24, 35, 70, 88, 120, 155]
li = [li[i] for i in range(len(li)) if i < 1 or i > 3]
print(li)
```

Result

```python
[12, 88, 120, 155]
```

## Question 84

> **_By using list comprehension, please write a program generate a 3*5*8 3D array whose each element is 0._**  

---
My Solution

```python
array = [[[0 for col in range(8)] for col in range(5)] for row in range(3)]
print(array)
```

Result

```python
[[[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]], [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]], [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]]
```

## Question 85

> **_By using list comprehension, please write a program to print the list after removing the 0th,4th,5th numbers in [12,24,35,70,88,120,155]._**  

---
My Solution

```python
li = [12,24,35,70,88,120,155]
li = [li[i] for i in range(len(li)) if i not in (0,4,5)]
print(li)
```

Result

```python
[24, 35, 70, 155]
```

## Question 86

> **_By using list comprehension, please write a program to print the list after removing the value 24 in [12,24,35,24,88,120,155]._**  

---
My Solution

```python
li = [12,24,35,24,88,120,155]
li = [x for x in li if x!=24]
print(li)
```

Result

```python
[12, 35, 88, 120, 155]
```

## Question 87

> **_With two given lists [1,3,6,78,35,55] and [12,24,35,24,88,120,155], write a program to make a list whose elements are intersection of the above given lists._**  

---
My Solution

```python
list1 = [1, 3, 6, 78, 35, 55]
list2 = [12, 24, 35, 24, 88, 120, 155]
set1 = set(list1)
set2 = set(list2)
intersection = set1 & set2
print(intersection)
```

Result

```python
{35}
```

## Question 88

> **_With a given list [12,24,35,24,88,120,155,88,120,155], write a program to print this list after removing all duplicate values with original order reserved._**  

---
My Solution

```python
li = [12, 24, 35, 24, 88, 120, 155, 88, 120, 155]
for i in li:
    if li.count(i) > 1:
        li.remove(i)
print(li)
```

Result

```python
[12, 35, 24, 88, 120, 155]
```

## Question 89

> **_Define a class Person and its two child classes: Male and Female. All classes have a method "getGender" which can print "Male" for Male class and "Female" for Female class._**  

---
My Solution

```python
class Person(object):
    def __init__(self):
        self.gender = "unknown"

    def getGender(self):
        print(self.gender)


class Male(Person):
    def __init__(self):
        self.gender = "Male"


class Female(Person):
    def __init__(self):
        self.gender = "Female"


sharon = Female()
doug = Male()
sharon.getGender()
doug.getGender()
```

Result

```python
Female
Male
```

## Question 90

> **_Please write a program which count and print the numbers of each character in a string input by console._**  

---
My Solution

```python
import string

s = input()
for letter in string.ascii_lowercase:
    cnt = s.count(letter)
    if cnt > 0:
        print(f'{letter},{cnt}')
```

Result

```python
jfsdlkdfjls
d,2
f,2
j,2
k,1
l,2
s,2
```

[**Previous: Q71-80**](https://github.com/polo871209/break-the-ice-with-python/blob/main/md/Question%2071-80.md "Q71-80")  
[**Next: Q91-100**](https://github.com/polo871209/break-the-ice-with-python/blob/main/md/Question%2091-100.md "Q91-100")  
[**Home**](https://github.com/polo871209/break-the-ice-with-python "home")
