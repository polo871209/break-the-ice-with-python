# Question 21-30

## Question 21

> **_A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. The trace of robot movement is shown as the following:_**

```python
UP 5
DOWN 3
LEFT 3
RIGHT 2
```

> **_The numbers after the direction are steps. Please write a program to compute the distance from current position after a sequence of movement and original point. If the distance is a float, then just print the nearest integer._**  
> **_Example:_**  
> **_If the following tuples are given as input to the program:_**

```python
UP 5
DOWN 3
LEFT 3
RIGHT 2
```

> **_Then, the output of the program should be:_**

```python
2
```

---
My Solution

```python
def q21():
    lst = [0,0]
    while True:
        s = input().split()
        if not s:
            break
        elif s[0] == 'UP':
            lst[1] += int(s[1])
        elif s[0] == 'DOWN':
            lst[1] -= int(s[1])
        elif s[0] == 'LEFT':
            lst[0] += int(s[1])
        elif s[0] == 'RIGHT':
            lst[0] -= int(s[1])
    return round((lst[0]**2 + lst[1]**2)**(1/2))
```

Result

```python
print(q21())
UP 5
DOWN 3
LEFT 3
RIGHT 2

2
```

## Question 22

> **_Write a program to compute the frequency of the words from the input. The output should output after sorting the key alphanumerically._**  

---
My Solution

```python
def q22():
    s = input().split()
    ss = sorted(set(s))
    for i in ss:
        print(f'{i}: {s.count(i)}')
```

Result

```python
q22()
New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
2: 2
3.: 1
3?: 1
New: 1
Python: 5
Read: 1
and: 1
between: 1
choosing: 1
or: 2
to: 1
```

## Question 23

> **_Write a function which can calculate square value of number_**  

---
My Solution

```python
def q23(n):
    return n**2
```

Result

```python
print(q23(10))
100
```

## Question 24

> **_Python has many built-in functions, and if you do not know how to use it, you can read document online or find some books. But Python has a built-in document function for every built-in functions._**  
> **_Please write a program to print some Python built-in functions documents, such as abs(), int(), raw_input()_**  

---
My Solution

```python
def q24(n):
    return n.__doc__
```

Result

```python
print(q24(range))
Return an object that produces a sequence of integers from start (inclusive)
to stop (exclusive) by step.  range(i, j) produces i, i+1, i+2, ..., j-1.
start defaults to 0, and stop is omitted!  range(4) produces 0, 1, 2, 3.
These are exactly the valid indices for a list of 4 elements.
When step is given, it specifies the increment (or decrement).
```

## Question 25

> **_Define a class, which have a class parameter and have a same instance parameter._**  

---
My Solution

```python
class F1team:
    name = "F1team"

    def __init__(self, name=None):
        self.name = name
```

Result

```python
mercedes = F1team('Mercedes')
print(f'{F1team.name}: {mercedes.name}')

redbull = F1team('Redbull')
print(f'{F1team.name}: {redbull.name}')

F1team: Mercedes
F1team: Redbull
```

## Question 26

> **_Define a function which can compute the sum of two numbers._**  

---
My Solution

```python
def q26(n1, n2):
    return n1+n2
```

Result

```python
print(q26(1, 2))
3
```

## Question 27

> **_Define a function that can convert a integer into a string and print it in console._**  

---
My Solution

```python
def q27(n):
    return str(n)
```

Result

```python
print(type(q27(2)))
<class 'str'>
```

## Question 28

> **_Define a function that can receive two integer numbers in string form and compute their sum and then print it in console._**  

---
My Solution

```python
def q28(s1, s2):
    return int(s1)+int(s2)
```

Result

```python
print(q28('1','2'))
3
```

## Question 29

> **_Define a function that can accept two strings as input and concatenate them and then print it in console._**  

---
My Solution

```python
def q29(s1, s2):
    return str(s1)+str(s2)
```

Result

```python
print(q29(1, 2))
12
```

## Question 30

> **_Define a function that can accept two strings as input and print the string with maximum length in console. If two strings have the same length, then the function should print all strings line by line._**  

---
My Solution

```python
def q30(s1, s2):
    if len(s1) == len(s2):
        return f'{s1}\n{s2}'
    elif len(s1) > len(s2):
        return s1
    else:
        return s2
```

Result

```python
print(q30('1', '2'))
1
2
print(q30('10', '2222'))
2222
```

[**Previous: Q11-20**](https://github.com/polo871209/break-the-ice-with-python/blob/main/md/Question%2011-20.md "Q11-20")  
[**Next: Q31-40**](https://github.com/polo871209/break-the-ice-with-python/blob/main/md/Question%2031-40.md "Q31-40")  
[**Home**](https://github.com/polo871209/break-the-ice-with-python "home")
