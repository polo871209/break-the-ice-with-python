

from genericpath import samestat
import re


def q1():
    l = []
    for i in range(2000, 3201):
        if i % 7 == 0 and i % 5 != 0:
            l.append(i)
    return l


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


def q4():
    list = input().split(',')
    tupl = tuple(list)
    return list, tuple


class q5():
    def get_string(self):
        self.str = input()

    def print_string(self):
        print(self.str.upper())


# hi = q5()
# hi.get_string()
# hi.print_string()


def q6():
    try:
        C, H, result = 50, 30, []
        input_list = [int(x) for x in input().split(',')]
        for D in input_list:
            Q = round(((2*C*D)/H)**(1/2))
            result.append(Q)
        return result
    except ValueError as err:
        return err

print(q6())
