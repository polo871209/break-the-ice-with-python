# Question 1-3

## Question 1

> **_Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
> between 2000 and 3200 (both included).The numbers obtained should be printed in a comma-separated sequence on a single line._**  
---
My Solution*

```python
def q1():
    l = []
    for i in range(2000, 3201):
        if i % 7 == 0 and i % 5 != 0:
            l.append(i)
    return l
```

## Question 2

> **_Write a program which can compute the factorial of a given numbers.The results should be printed in a comma-separated sequence on a single line.Suppose the following input is supplied to the program: 8
> Then, the output should be:40320_**  
---
My Solution

```python
def q2(num):
    try:
        num = int(num)
        if num == 0:
            return 0
        sum = 1
        for i in range(1, num+1):
            sum *= i
        return sum
    except ValueError as err:
        return err
```

## Question 3

> **_With a given integral number n, write a program to generate a dictionary that contains (i, i x i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.Suppose the following input is supplied to the program: 8_**
> **_Then, the output should be:_**  

```python
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
```

---
My Solution

```python
def q3(num):
    try:
        num = int(num)
        if num == 0:
            return {0: 0}
        d = {}
        for i in range(1, num+1):
            d[i] = i*i
        return d
    except ValueError as err:
        return err
```

[**Go to next**](https://github.com/darkprinx/100-plus-Python-programming-exercises-extended/blob/master/Status/Day%202.md "Q10-20")
