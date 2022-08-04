def read_next(*args):
    for arg in args:
        for el in arg:
            yield el


for item in read_next("string", (2,), {"d": 1, "i": 2, "c": 3, "t": 4}):
    print(item, end='')
# string2dict

for i in read_next("Need", (2, 3), ["words", "."]):
    print(i)
# N
# e
# e
# d
# 2
# 3
# words
# .
