from functools import reduce
# Q1


def q1():
    l = []
    for i in range(2000, 3201):
        if i % 7 == 0 and i % 5 != 0:
            l.append(i)
    return l


# Q2
def q2(num):
    if num == 0:
        return 0
    sum = 1
    for i in range(1, num+1):
        sum *= i
    return sum


def q2_2(num):
    if num == 0:
        return 0
    list = [item for item in range(1, num+1)]
    return reduce(lambda acc, item: acc*item, list, 1)


# Q3
def q3(num):
    if num == 0:
        return {0: 0}
    d = {}
    for i in range(1, num+1):
        d[i] = i*i
    return d


# Q4
def q4():
    list = input().split(',')
    tupl = tuple(list)
    return list, tupl


# Q5
class q5():
    def get_string(self):
        self.str = input()

    def print_string(self):
        print(self.str.upper())


# hi = q5()
# hi.get_string()
# hi.print_string()


# Q6
def q6():
    C, H, result = 50, 30, []
    input_list = [int(x) for x in input().split(',')]
    for D in input_list:
        Q = round(((2*C*D)/H)**(1/2))
        result.append(Q)
    return result


# Q7
def q7(x, y):
    lst = []
    for i in range(x):
        temp = []
        for j in range(y):
            temp.append(i*j)
        lst.append(temp)
    return lst


# Q8
def q8():
    lst = [x for x in input().split(',')]
    lst.sort()
    return ','.join(lst)


# Q9
def q9():
    pass
