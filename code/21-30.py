# Q21
def q21():
    lst = [0, 0]
    while True:
        s = input().split()
        if not s:
            break
        elif s[0] == 'UP':
            lst[1] += int(s[1])
        elif s[0] == 'DOWN':
            lst[1] -= int(s[1])
        elif s[0] == 'LEFT':
            lst[0] += int(s[1])
        elif s[0] == 'RIGHT':
            lst[0] -= int(s[1])
    return round((lst[0]**2 + lst[1]**2)**(1/2))


# Q22
def q22():
    s = input().split()
    ss = sorted(set(s))
    for i in ss:
        print(f'{i}: {s.count(i)}')


# Q23
def q23(n):
    return n**2


# Q24
def q24(n):
    return n.__doc__


# Q25
class F1team:
    name = "F1team"

    def __init__(self, name=None):
        self.name = name

# mercedes=F1team('Mercedes')
# print(f'{F1team.name}: {mercedes.name}')

# redbull=F1team('Redbull')
# print(f'{F1team.name}: {redbull.name}')


# Q26
def q26(n1, n2):
    return n1+n2


# Q27
def q27(n):
    return str(n)


# Q28
def q28(s1, s2):
    return int(s1)+int(s2)


# Q29
def q29(s1, s2):
    return str(s1)+str(s2)


# Q30
def q30(s1, s2):
    if len(s1) == len(s2):
        return f'{s1}\n{s2}'
    elif len(s1) > len(s2):
        return s1
    else:
        return s2
