# import pandas as pd
#
#
# def add(*args):
#     x = []
#     for i in args:
#         x.append(i)
#     pandas_dataframe = pd.DataFrame(x)
#
#     sum = pandas_dataframe.sum()[0]
#     return sum
#
#
# print(add(3,5,7,8))

#
# def add(*args):
#     sum = 0
#     for x in args:
#         sum = sum + x
#     return sum
#
#
# print(add(3, 5, 8))


def add(**strick):
    print(strick)

    for kye, value in strick.items():
        print(kye)
        print(value)



add(add=5, multiply=3)