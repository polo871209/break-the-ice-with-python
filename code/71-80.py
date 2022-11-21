# Q71
import datetime
import zlib
import random
resp = [i for i in range(10, 151) if i % 35 == 0]
print(random.choice(resp))


# Q72
resp = random.sample(range(100, 201), 5)
print(resp)


# Q73
resp = random.sample(range(100, 201, 2), 5)
print(resp)


# Q74
lst = [i for i in range(1, 1001) if i % 35 == 0]
resp = random.sample(lst, 5)
print(resp)


# Q75
print(random.randrange(7, 16))


# Q76
s = 'hello world!hello world!hello world!hello world!'
b = bytes(s, 'utf-8')
c = zlib.compress(b)
print(c)
print(zlib.decompress(c))


# Q77

before = datetime.datetime.now()
for i in range(100):
    x = 1 + 1
after = datetime.datetime.now()
execution_time = after - before
print(execution_time.microseconds)


# Q78

lst = [3, 6, 7, 8]
random.shuffle(lst)
print(lst)


# Q79
subjects = ["I", "You"]
verbs = ["Play", "Love"]
objects = ["Hockey", "Football"]

for sub in subjects:
    for verb in verbs:
        for obj in objects:
            print("{} {} {}".format(sub, verb, obj))


# Q80
li = [5, 6, 77, 45, 22, 12, 24]
lst = list(filter(lambda n: n % 2 != 0, li))
print(lst)
