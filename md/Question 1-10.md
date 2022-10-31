# Question 1-10

## Question 1

> **_Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
> between 2000 and 3200 (both included).The numbers obtained should be printed in a comma-separated sequence on a single line._**  
---
My Solution

```python
def q1():
    l = []
    for i in range(2000, 3201):
        if i % 7 == 0 and i % 5 != 0:
            l.append(i)
    return l
```

Result

```python
print(q1())
[2016, 2023, 2037, 2044, 2051, 2058, 2072, 2079, 2086, 2093, 2107, 2114, 2121, 2128, 2142, 2149, 2156, 2163, 2177, 2184, 2191, 2198, 2212, 2219, 2226, 2233, 2247, 2254, 2261, 2268, 2282, 2289, 2296, 2303, 2317, 2324, 2331, 2338, 2352, 2359, 2366, 2373, 2387, 2394, 2401, 2408, 2422, 2429, 2436, 2443, 2457, 2464, 2471, 2478, 2492, 2499, 2506, 2513, 2527, 2534, 2541, 2548, 2562, 2569, 2576, 2583, 2597, 2604, 2611, 2618, 2632, 2639, 2646, 2653, 2667, 2674, 2681, 2688, 2702, 2709, 2716, 2723, 2737, 2744, 2751, 2758, 2772, 2779, 2786, 2793, 2807, 2814, 2821, 2828, 2842, 2849, 2856, 2863, 2877, 2884, 2891, 2898, 2912, 2919, 2926, 2933, 2947, 2954, 2961, 2968, 2982, 2989, 2996, 3003, 3017, 3024, 3031, 3038, 3052, 3059, 3066, 3073, 3087, 3094, 3101, 3108, 3122, 3129, 3136, 3143, 3157, 3164, 3171, 3178, 3192, 3199]
```

## Question 2

> **_Write a program which can compute the factorial of a given numbers.The results should be printed in a comma-separated sequence on a single line.Suppose the following input is supplied to the program: 8
> Then, the output should be:40320_**  
---
My Solution

```python
def q2(num):
        if num == 0:
            return 0
        sum = 1
        for i in range(1, num+1):
            sum *= i
        return sum
```

Result

```python
print(q2(8))
40320
print(q2(10))
3628800
```

My Solution: lambda/reduce

```python
from functools import reduce
def q2_2(num):
        if num == 0:
            return 0
        list = [item for item in range(1, num+1)]
        return reduce(lambda acc, item: acc*item, list, 1)
```

Result

```python
print(q2_2(8))
40320
print(q2_2(10))
3628800
```

## Question 3

> **_With a given integral number n, write a program to generate a dictionary that contains (i, i x i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary._**

---
My Solution

```python
def q3(num):
        if num == 0:
            return {0: 0}
        d = {}
        for i in range(1, num+1):
            d[i] = i*i
        return d
```

Result

```python
print(q3(10))
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}
```

## Question 4

> **_Write a program which accepts a sequence of comma-separated string from console and generate a list and a tuple which contains every string._**  

---
My Solution

```python
def q4():
    list = input().split(',')
    tupl = tuple(list)
    return list, tupl
```

Result

```python
print(q4())
123,abc,7732,sada 
(['123', 'abc', '7732', 'sada'], ('123', 'abc', '7732', 'sada'))
```

## Question 5

> **_Define a class which has at least two methods:_**
>
> - **_getString: to get a string from console input_**
> - **_printString: to print the string in upper case._**  
> **_Also please include simple test function to test the class methods._**

---
My Solution

```python
class q5():
    def get_string(self):
        self.str = input()

    def print_string(self):
        print(self.str.upper())

hi = q5()
hi.get_string()
hi.print_string()
```

Result

```python
print(q5())
1q231
1Q231
```

## Question 6

> **_Write a program that calculates and prints the value according to the given formula:_**  
> **_Q = Square root of [(2xCxD)/H]_**  
> **_Following are the fixed values of C and H:_**  
> **_C is 50. H is 30._**  
> **_D is the variable whose values should be input to your program in a comma-separated sequence._**  

---
My Solution

```python
def q6():
        C, H, result = 50, 30, []
        input_list = [int(x) for x in input().split(',')]
        for D in input_list:
            Q = round(((2*C*D)/H)**(1/2))
            result.append(Q)
        return result
```

Result

```python
print(q6())
100,150,180
[18, 22, 24]
```

## Question 7

> **_Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i _ j.\***  
> **_Note: i=0,1.., X-1; j=0,1,¡­Y-1. Suppose the following inputs are given to the program: 3,5_**  
> **_Then, the output of the program should be:_**

```python
[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]
```
---
My Solution

```python
def q7(x, y):
    lst = []
    for i in range(x):
        temp = []
        for j in range(y):
            temp.append(i*j)
        lst.append(temp)
    return lst
```

Result

```python
print(q7(2,5))
[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4]]
print(q7(5,2))
[[0, 0], [0, 1], [0, 2], [0, 3], [0, 4]]
```

## Question 8

> **_Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically._**
---
My Solution

```python
def q8():
    lst = [x for x in input().split(',')]
    lst.sort()
    return ','.join(lst)
```

Result

```python
print(q8())
without,hello,bag,world
bag,hello,without,world
```

## Question 9

> **_Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized._**

---
My Solution

```python
def q9():
    inputs = input()
    return inputs.upper()
```

Result

```python
print(q9())
hi i am po
HI I AM PO
```

## Question 10

> **_Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically._**

---
My Solution

```python
def q10():
    inputs = input().split()
    return ' '.join(sorted(list(set(inputs))))
```

Result

```python
print(q10())
hello world and practice makes perfect and hello world again
again and hello makes perfect practice world
```

[**Next: Q11-20**](https://github.com/polo871209/break-the-ice-with-python/blob/main/md/Question%2011-20.md "Q11-20")
