# Question 91-100

## Question 91

> **_Please write a program which count and print the numbers of each character in a string input by console._**  

---
My Solution

```python
import string

s = input()
for letter in string.ascii_lowercase:
    cnt = s.count(letter)
    if cnt > 0:
        print(f"{letter},{cnt}")
```

Result

```python
str: dsfgsrsf
d,1
f,2
g,1
r,1
s,3
```

## Question 92

> **_Please write a program which accepts a string from console and print it in reverse order._**  

---
My Solution

```python
s = "H1e2l3l4o5w6o7r8l9d"
s = [ s[i] for i in range(len(s)) if i%2 ==0 ]
print(''.join(s))
```

Result

```python
Helloworld
```

## Question 93

> **_Please write a program which prints all permutations of [1,2,3]_**  

---
My Solution

```python
import itertools
print(list(itertools.permutations([1, 2, 3])))
```

Result

```python
[(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]
```

## Question 94

> **_Write a program to solve a classic ancient Chinese puzzle: We count 35 heads and 94 legs among the chickens and rabbits in a farm. How many rabbits and how many chickens do we have?_**  

---
My Solution

```python
def solve(numheads,numlegs):
    ns='No solutions!'
    for i in range(numheads+1):
        j=numheads-i
        if 2*i+4*j==numlegs:
            return i,j
    return ns,ns

numheads = 35
numlegs = 94
solutions=solve(numheads,numlegs)
print(solutions)

```

Result

```python
(23, 12)
```

## Question 95

> **__**  

---
My Solution

```python

```

Result

```python

```

## Question 96

> **__**  

---
My Solution

```python

```

Result

```python

```

## Question 97

> **__**  

---
My Solution

```python

```

Result

```python

```

## Question 98

> **__**  

---
My Solution

```python

```

Result

```python

```

## Question 99

> **__**  

---
My Solution

```python

```

Result

```python

```

## Question 100

> **__**  

---
My Solution

```python

```

Result

```python

```

[**Previous: Q81-90**](https://github.com/polo871209/break-the-ice-with-python/blob/main/md/Question%2081-90.md "Q81-90")  
[**Home**](https://github.com/polo871209/break-the-ice-with-python "home")
