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
# Q14
# Q15
# Q16
# Q17
# Q18
# Q19
# Q20
