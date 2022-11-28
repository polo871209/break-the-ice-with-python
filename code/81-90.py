# Q81
li = [12, 24, 35, 70, 88, 120, 155]
li = [x for x in li if x % 35 != 0]
print(li)


# Q82
li = [12, 24, 35, 70, 88, 120, 155]
li = [li[i] for i in range(len(li)) if i % 2 != 0 and i <= 6]
print(li)


# Q83
li = [12, 24, 35, 70, 88, 120, 155]
li = [li[i] for i in range(len(li)) if i < 1 or i > 3]
print(li)


# Q84
array = [[[0 for col in range(8)] for col in range(5)] for row in range(3)]
print(array)


# Q85
li = [12, 24, 35, 70, 88, 120, 155]
li = [li[i] for i in range(len(li)) if i not in (0, 4, 5)]
print(li)


# Q86
li = [12, 24, 35, 24, 88, 120, 155]
li = [x for x in li if x != 24]
print(li)


# Q87
list1 = [1, 3, 6, 78, 35, 55]
list2 = [12, 24, 35, 24, 88, 120, 155]
set1 = set(list1)
set2 = set(list2)
intersection = set1 & set2
print(intersection)


# Q88
li = [12, 24, 35, 24, 88, 120, 155, 88, 120, 155]
for i in li:
    if li.count(i) > 1:
        li.remove(i)
print(li)


# Q89
class Person(object):
    def __init__(self):
        self.gender = "unknown"

    def getGender(self):
        print(self.gender)


class Male(Person):
    def __init__(self):
        self.gender = "Male"


class Female(Person):
    def __init__(self):
        self.gender = "Female"


sharon = Female()
doug = Male()
sharon.getGender()
doug.getGender()


# Q90
import string

s = input()
for letter in string.ascii_lowercase:
    cnt = s.count(letter)
    if cnt > 0:
        print(f'{letter},{cnt}')
