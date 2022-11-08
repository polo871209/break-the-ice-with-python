# Question 51-60

## Question 51

> **_Write a function to compute 5/0 and use try/except to catch the exceptions._**  

---
My Solution

```python
def divide():
    return 5/0

try:
    divide()
except ZeroDivisionError as err:
    print("Why on earth you are dividing a number by ZERO!!")
except:
    print("Any other exception")
```

Result

```python
Why on earth you are dividing a number by ZERO!!
```

## Question 52

> **_Define a custom exception class which takes a string message as attribute._**  

---
My Solution

```python
class CustomException(Exception):
    """Exception raised for custom purpose

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message):
        self.message = message


hero = input('Who is your favorite MARVLE hero: ')

try:
    if hero.lower() == 'spiderman':
        print('SpiderMan is the only truth!')
    else:
        raise CustomException(
            'You must be crazy...Only SpiderMan is the true hero!')
except CustomException as err:
    print(err.message)
```

Result

```python
Who is your favorite MARVLE hero: spiderman
SpiderMan is the only truth!
Who is your favorite MARVLE hero: CaptainAmerica
You must be crazy...Only SpiderMan is the true hero!
```

## Question 53

> **_Assuming that we have some email addresses in the "username@companyname.com" format, please write program to print the user name of a given email address. Both user names and company names are composed of letters only._**  

---
My Solution

```python
import re


def q53(target_string):
    return re.search(r'([A-Za-z0-9]+[.-_]*[A-Za-z0-9]+)@',
                     target_string).group(1)
```

Result

```python
print(q53('qazh0123@gmail.com'))
qazh0123
```

## Question 54

> **_Assuming that we have some email addresses in the "username@companyname.com" format, please write program to print the company name of a given email address. Both user names and company names are composed of letters only._**  

---
My Solution

```python
def q54(target_string):
    return re.search(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@([A-Za-z0-9-]+)\.[A-Z|a-z]{2,}', target_string).group(2)
```

Result

```python
print(q54('qazh0123@gmail.com'))
gmail
```

## Question 55

> **_Write a program which accepts a sequence of words separated by whitespace as input to print the words composed of digits only._**  

---
My Solution

```python
str = input().split()
ans = [word for word in str if word.isdigit()]  #
print(ans)
```

Result

```python
2 cats and 3 dogs.
['2', '3']
```

## Question 56

> **_Print a unicode string "hello world"._**  

---
My Solution

```python
print(u'hello world!')
```

Result

```python
hello world!
```

## Question 57

> **_Write a program to read an ASCII string and to convert it to a unicode string encoded by utf-8._**  

---
My Solution

```python
s = input()
u = s.encode('utf-8')
print(u)
```

Result

```python
PythØn
b'Pyth\xc3\x98n'
```

## Question 58

> **_Write a special comment to indicate a Python source code file is in unicode._**  

---
My Solution

```python
# -*- coding: utf-8 -*-
```

## Question 59

> **_Write a program to compute 1/2+2/3+3/4+...+n/n+1 with a given n input by console (n>0)._**  

---
My Solution

```python
def q59():
    n = int(input())
    total = 0
    for i in range(1,n+1):
        res = i/(i+1)
        total += res
    return round(total, 2)
```

Result

```python
5
3.55
```

## Question 60

> **_Write a program to compute:_**  
```python
f(n)=f(n-1)+100 when n>0
and f(0)=0
```

--- 
My Solution

```python
def f(n):
    if n == 0:
        return 0
    return f(n-1) + 100

n = int(input())
print(f(n))
```

Result

```python
5
500
```

[**Previous: Q41-50**](https://github.com/polo871209/break-the-ice-with-python/blob/main/md/Question%2041-50.md "Q41-50")  
[**Next: Q61-70**](https://github.com/polo871209/break-the-ice-with-python/blob/main/md/Question%2061-70.md "Q61-70")  
[**Home**](https://github.com/polo871209/break-the-ice-with-python "home")
