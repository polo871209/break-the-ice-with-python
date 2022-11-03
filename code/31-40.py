# Q31
def q31():
    dict = {i: i**2 for i in range(1, 21)}
    return dict


# Q32
def q32():
    dict = {i: i**2 for i in range(1, 21)}
    return dict.keys()


# Q33
def q33():
    lst = [i ** 2 for i in range(1, 21)]
    print(lst)


# Q34
def q34():
    lst = [i ** 2 for i in range(1, 21)]
    print(lst[:5])


# Q35
def q35():
    lst = [i ** 2 for i in range(1, 21)]
    print(lst[-5:])


# Q36
def q36():
    lst = [i ** 2 for i in range(1, 21)]
    print(lst[5:])


# Q37
def q37():
    lst = [i ** 2 for i in range(1, 21)]
    print(tuple(lst))


# Q38
def q38():
    tpl = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    return f'{tpl[:5]}\n{tpl[5:]}'


# Q39
def q39():
    tpl = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    return tuple([i for i in tpl if i % 2 == 0])


# Q40
def q40(s):
    if s.upper() == "YES":
        return 'Yes'
    else:
        return 'No'
