# Question 31-40

## Question 31

> **_Define a function which can print a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys._**  

---
My Solution

```python
def q31():
    dict = {i: i**2 for i in range(1, 21)}
    return dict
```

Result

```python
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225, 16: 256, 17: 289, 18: 324, 19: 361, 20: 400}
```

## Question 32

> **_Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys. The function should just print the keys only._**  

---
My Solution

```python
def q32():
    dict = {i: i**2 for i in range(1, 21)}
    return dict.keys()
```

Result

```python
print(q32())
dict_keys([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
```

## Question 33

> **_Define a function which can generate and print a list where the values are square of numbers between 1 and 20 (both included)._**  

---
My Solution

```python
def q33():
    lst = [i ** 2 for i in range(1, 21)]
    print(lst)
```

Result

```python
q33()
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400]
```

## Question 34

> **_Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). Then the function needs to print the first 5 elements in the list._**  

---
My Solution

```python
def q34():
    lst = [i ** 2 for i in range(1, 21)]
    print(lst[:5])
```

Result

```python
q34()
[1, 4, 9, 16, 25]
```

## Question 35

> **_Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). Then the function needs to print the last 5 elements in the list._**  

---
My Solution

```python
def q35():
    lst = [i ** 2 for i in range(1, 21)]
    print(lst[-5:])
```

Result

```python
q35()
[256, 289, 324, 361, 400]
```

## Question 36

> **_Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). Then the function needs to print all values except the first 5 elements in the list._**  

---
My Solution

```python
def q36():
    lst = [i ** 2 for i in range(1, 21)]
    print(lst[5:])
```

Result

```python
q36()
[36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400]
```

## Question 37

> **_Define a function which can generate and print a tuple where the value are square of numbers between 1 and 20 (both included)._**  

---
My Solution

```python
def q37():
    lst = [i ** 2 for i in range(1, 21)]
    print(tuple(lst))
```

Result

```python
q37()
(1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400)
```

## Question 38

> **_With a given tuple (1,2,3,4,5,6,7,8,9,10), write a program to print the first half values in one line and the last half values in one line._**  

---
My Solution

```python
def q38():
    tpl = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    return f'{tpl[:5]}\n{tpl[5:]}'
```

Result

```python
print(q38())
(1, 2, 3, 4, 5)
(6, 7, 8, 9, 10)
```

## Question 39

> **_Write a program to generate and print another tuple whose values are even numbers in the given tuple (1,2,3,4,5,6,7,8,9,10)._**  

---
My Solution

```python
def q39():
    tpl = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    return tuple([i for i in tpl if i % 2 == 0])
```

Result

```python
print(q39())
(2, 4, 6, 8, 10)
```

## Question 40

> **_Write a program which accepts a string as input to print "Yes" if the string is "yes" or "YES" or "Yes", otherwise print "No"._**  

---
My Solution

```python
def q40(s):
    if s.upper() == "YES":
        return 'Yes'
    else:
        return 'No'
```

Result

```python
print(q40('yes'))
print(q40('asda'))
Yes
No
```

[**Previous: Q21-30**](https://github.com/polo871209/break-the-ice-with-python/blob/main/md/Question%2021-30.md "Q21-30")  
[**Next: Q41-50**](https://github.com/polo871209/break-the-ice-with-python/blob/main/md/Question%2041-50.md "Q41-50")  
[**Home**](https://github.com/polo871209/break-the-ice-with-python "home")
