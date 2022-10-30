

from genericpath import samestat


def q1():
    """
    Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included).The numbers obtained should be printed in a comma-separated sequence on a single line.

    Returns:
        divisible by 7 but are not a multiple of 5, between 2000 and 3200
    """
    l = []
    for i in range(2000, 3201):
        if i % 7 == 0 and i % 5 != 0:
            l.append(i)
    return l


def q2(num):
    """
    Write a program which can compute the factorial of a given numbers.The results should be printed in a comma-separated sequence on a single line.Suppose the following input is supplied to the program: 8 Then, the output should be:40320

    Args:
        num (int)

    Returns:
        factorial num
    """
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
    """
    With a given integral number num, write a program to generate a dictionary that contains (i, i x i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary

    Args:
        num (int)

    Returns:
        factorial num
    """
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
