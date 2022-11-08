# Q51
import re


def divide():
    return 5/0


try:
    divide()
except ZeroDivisionError as err:
    print("Why on earth you are dividing a number by ZERO!!")
except:
    print("Any other exception")


# Q52
class CustomException(Exception):
    """Exception raised for custom purpose

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message):
        self.message = message


hero = input('Who is your favorite MARVLE hero: ')

try:
    if hero.lower() == 'spiderman':
        print('SpiderMan is the only truth!')
    else:
        raise CustomException(
            'You must be crazy...Only SpiderMan is the true hero!')
except CustomException as err:
    print(err.message)


# Q53
def q53(target_string):
    return re.search(r'([A-Za-z0-9]+[.-_]*[A-Za-z0-9]+)@',
                     target_string).group(1)


# Q54
def q54(target_string):
    return re.search(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@([A-Za-z0-9-]+)\.[A-Z|a-z]{2,}', target_string).group(2)


# Q55
str = input().split()
ans = [word for word in str if word.isdigit()]  #
print(ans)


# Q56
print(u'hello world!')


# Q57
s = input()
u = s.encode('utf-8')
print(u)


# Q58
# -*- coding: utf-8 -*-


# Q59
def q59():
    n = int(input())
    total = 0
    for i in range(1, n+1):
        res = i/(i+1)
        total += res
    return round(total, 2)


# Q60
def f(n):
    if n == 0:
        return 0
    return f(n-1) + 100


n = int(input())
print(f(n))
