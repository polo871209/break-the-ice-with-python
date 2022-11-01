# Q11
def q11(*args):
    lst = []
    for x in [int(str(i), 2) for i in args]:
        if x % 5 == 0:
            lst.append(str(bin(x)[2:]))
    res = ','.join(lst)
    return res


# Q12
def q12():
    lst = []
    for i in range(1000, 3001):
        if i % 2 == 0:
            lst.append(str(i))
    return ','.join(lst)


# Q13
def q13():
    digits, letters = 0, 0
    for i in input().split():
        try:
            int(i)
            digits += len(i)
        except:
            letters += len(i)
    return digits, letters


# Q14
def q14():
    word = input()
    lower, upper = 0, 0
    for i in word:
        lower += i.islower()
        upper += i.isupper()
    return lower, upper


# Q15
def q15(a):
    return a+a*11+a*111+a*1111


# Q16

# Q17
# Q18
# Q19
# Q20
