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

#
# def add(**kwargs):
#     print(kwargs)
#
#     for kye, value in kwargs.items():
#         print(kye)
#         print(value)
#
#
# add(add=5, multiply=3)

class Car:

    def __init__(self, **kwargs):
        self.company = kwargs['company']
        self.color = kwargs['color']
        self.mirror = kwargs['mirror']


car_object = Car(color=5, mirror="2 mirror")


print(type(car_object.color))
print(car_object.color)
