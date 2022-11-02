import re


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
def q16():
    lst = []
    for i in input().split(','):
        if int(i) % 2 != 0:
            lst.append(str(int(i)**2))
    return ','.join(lst)


# Q17
def q17():
    amount = 0
    for way, amount in input().split():
        if way == 'D':
            amount += amount
        elif way == 'W':
            amount -= amount
    return amount


# Q18
def q18(*args):
    pattern = re.compile(
        r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$#@])[A-Za-z\d@$!#%*?&]{6,12}$")
    valid_pass = []
    for string in args:
        a = pattern.search(string)
        if a is None:
            continue
        else:
            valid_pass.append(string)
    return ','.join(valid_pass)


# Q19
def q19():
    lst = []
    while True:
        input_str = input().split(',')
        if not input_str[0]:                          
            break
        lst.append(tuple(input_str))

    lst.sort(key= lambda x:(x[0],int(x[1]),int(x[2]))) 
    return lst


# Q20
