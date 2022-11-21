# Q61
import random


def f(n):
    if n < 2:
        return n
    return f(n-1) + f(n-2)


n = int(input())
print(f(n))


# Q62
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


# Q63
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


# Q64
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


# Q65
data = [2, 4, 5, 6, ]
for i in data:
    assert i % 2 == 0, f'{i} is not an even number'


# Q66
expression = input()
ans = eval(expression)
print(ans)


# Q67
# Q68
rand_num = random.uniform(10, 100)
print(rand_num)


# Q69
rand_num = random.uniform(5, 95)
print(rand_num)


# Q70
resp = [i for i in range(0, 11, 2)]
print(random.choice(resp))
