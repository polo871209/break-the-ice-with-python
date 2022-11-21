# Question 71-80

## Question 71

> **_Please write a program to output a random number, which is divisible by 5 and 7, between 10 and 150 inclusive using random module and list comprehension._**  

---
My Solution

```python
import random
resp = [i for i in range(10,151) if i % 35 == 0 ]
print(random.choice(resp))
```

## Question 72

> **_Please write a program to generate a list with 5 random numbers between 100 and 200 inclusive._**  

---
My Solution

```python
import random
resp = random.sample(range(100,201),5)
print(resp)
```

Result

```python
funprojects/test.py
[128, 111, 176, 107, 189]
```

## Question 73

> **_Please write a program to randomly generate a list with 5 even numbers between 100 and 200 inclusive._**  

---
My Solution

```python
import random
resp = random.sample(range(100,201,2),5)
print(resp)
```

Result

```python
[142, 132, 128, 146, 100]
```

## Question 74

> **_Please write a program to randomly generate a list with 5 numbers, which are divisible by 5 and 7 , between 1 and 1000 inclusive._**  

---
My Solution

```python
import random
lst = [i for i in range(1,1001) if i%35 == 0]
resp = random.sample(lst,5)
print(resp)
```

Result

```python
[385, 665, 945, 630, 770]
```

## Question 75

> **_Please write a program to randomly print a integer number between 7 and 15 inclusive._**  

---
My Solution

```python
import random
print random.randrange(7,16)
```

## Question 76

> **_Please write a program to compress and decompress the string "hello world!hello world!hello world!hello world!"._**  

---
My Solution

```python
import zlib
s = 'hello world!hello world!hello world!hello world!'
b = bytes(s, 'utf-8')
c = zlib.compress(b)
print(c)
print(zlib.decompress(c))
```

Result

```python
b'x\x9c\xcbH\xcd\xc9\xc9W(\xcf/\xcaIQ\xcc \x82\r\x00\xbd[\x11\xf5'
b'hello world!hello world!hello world!hello world!'
```

## Question 77

> **_Please write a program to print the running time of execution of "1+1" for 100 times._**  

---
My Solution

```python
import datetime

before = datetime.datetime.now()
for i in range(100):
    x = 1 + 1
after = datetime.datetime.now()
execution_time = after - before
print(execution_time.microseconds)
```

Result

```python
12(microseconds)    
```

## Question 78

> **_Please write a program to shuffle and print the list [3,6,7,8]._**  

---
My Solution

```python
import random

lst = [3,6,7,8]
random.shuffle(lst)
print(lst)
```

Result

```python
[8, 6, 7, 3]
```

## Question 79

> **_Please write a program to generate all sentences where subject is in ["I", "You"] and verb is in ["Play", "Love"] and the object is in ["Hockey","Football"]._**  

---
My Solution

```python
subjects=["I", "You"]
verbs=["Play", "Love"]
objects=["Hockey","Football"]

for sub in subjects:
    for verb in verbs:
        for obj in objects:
            print("{} {} {}".format(sub,verb,obj))
```

Result

```python
I Play Hockey
I Play Football
I Love Hockey
I Love Football
You Play Hockey
You Play Football
You Love Hockey
You Love Football
```

## Question 80

> **_Please write a program to print the list after removing even numbers in [5,6,77,45,22,12,24]._**  

---
My Solution

```python
li = [5, 6, 77, 45, 22, 12, 24]
lst = list(filter(lambda n: n % 2 != 0, li))
print(lst)

```

Result

```python
[5, 77, 45]
```

[**Previous: Q61-70**](https://github.com/polo871209/break-the-ice-with-python/blob/main/md/Question%2061-70.md "Q61-70")  
[**Next: Q81-90**](https://github.com/polo871209/break-the-ice-with-python/blob/main/md/Question%2081-90.md "Q81-90")  
[**Home**](https://github.com/polo871209/break-the-ice-with-python "home")
