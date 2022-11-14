# Question 61-70

## Question 61

> **_The Fibonacci Sequence is computed based on the following formula:_**  
```python
f(n)=0 if n=0
f(n)=1 if n=1
f(n)=f(n-1)+f(n-2) if n>1
```
> **_Please write a program to compute the value of f(n) with a given n input by console._** 

---
My Solution

```python
def f(n):
    if n < 2:
        return n
    return f(n-1) + f(n-2)

n = int(input())
print(f(n))
```

Result

```python
7
13
```

## Question 62

> **_The Fibonacci Sequence is computed based on the following formula:_**  
```python
f(n)=0 if n=0
f(n)=1 if n=1
f(n)=f(n-1)+f(n-2) if n>1
```
> **_Please write a program to compute the value of f(n) with a given n input by console._**  

---
My Solution

```python
def f(n):
    if n < 2:
        fibo[n] = n
        return fibo[n]
    fibo[n] = f(n-1) + f(n-2)
    return fibo[n]

n = int(input())
fibo = [0]*(n+1) 
f(n)              
fibo = [str(i) for i in fibo]   
ans = ",".join(fibo)   
print(ans)
```

Result

```python
7
0,1,1,2,3,5,8,13
```

## Question 63

> **_Please write a program using generator to print the even numbers between 0 and n in comma separated form while n is input by console._**  

---
My Solution

```python
def q63(n):
    i = 0
    while i <= n:
        if i % 2 == 0:
            yield i
        i += 1


n = int(input())
values = []
for i in q63(n):
    values.append(str(i))

print(','.join(values))
```

Result

```python
10
0,2,4,6,8,10
```

## Question 64

> **_Please write a program using generator to print the numbers which can be divisible by 5 and 7 between 0 and n in comma separated form while n is input by console._**  

---
My Solution

```python
def q64(n):
    i = 0
    while i <= n:
        if i % 5 == 0 and i % 7 == 0:
            yield i
        i += 1


n = int(input())
values = []
for i in q64(n):
    values.append(str(i))

print(','.join(values))
```

Result

```python
100
0,35,70
```

## Question 65

> **_Please write assert statements to verify that every number in the list [2,4,6,8] is even._**  

---
My Solution

```python
data = [2, 4, 5, 6,]
for i in data:
    assert i % 2 == 0, f'{i} is not an even number'

```

Result

```python
    assert i % 2 == 0, f'{i} is not an even number'
AssertionError: 5 is not an even number
```

## Question 66

> **_Please write a program which accepts basic mathematic expression from console and print the evaluation result._**  

---
My Solution

```python
expression = input()
ans = eval(expression)
print(ans)
```

Result

```python
35 + 3
38
```

## Question 67

> **_Write a binary search function which searches an item in a sorted list. The function should return the index of element to be searched in the list._**  

---
My Solution

```python

```

Result

```python

```

## Question 68

> **__**  

---
My Solution

```python

```

Result

```python

```

## Question 69

> **__**  

---
My Solution

```python

```

Result

```python

```

## Question 70

> **__**  

---
My Solution

```python

```

Result

```python

```

[**Previous: Q51-60**](https://github.com/polo871209/break-the-ice-with-python/blob/main/md/Question%2051-60.md "Q51-60")  
[**Next: Q71-80**](https://github.com/polo871209/break-the-ice-with-python/blob/main/md/Question%2071-80.md "Q71-80")  
[**Home**](https://github.com/polo871209/break-the-ice-with-python "home")
