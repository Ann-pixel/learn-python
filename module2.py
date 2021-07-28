# import module1
# from module1 import (
#     multiply,
#     divide,
# )  # not recommended. be explicit in what you want to avoid conflict.
# import shopping.shopping_cart  # shopping- the folder is a package. syntax- package.module

# from shopping.more_shopping.more_shopping_cart import (
#     welcome,
# )  # from package.package.... module import func.

# # once this runs, it makes a pycache folder to save the module into. so the import runs only the first time or anytime a module changes.
# # print(module1)
# # print(module1.divide(4, 2))  # 2.0
# print(shopping.shopping_cart.shop("book"))  # ['book']
# welcome()  # Great import.

# print(multiply(2, 3))
# print(divide(2, 3))


# __name__ & __main__

# each file gets a __name__ attribute. the entry point of the app gets __main__ as its name. rest keep their given names with relative path.

# print(__name__)  # upon running python module2.py # __main__
# # meaning that this is the main file we're running. all others are modules that we import.
# # can be used in something like:
# if __name__ == "__main__":  # run only if this is the main file.
#     print("please run this.")


# built-in MODULES & PACKAGES - python module index

# installing python on the mc installs all these modules. so to use them we just import them in our files.

# import random
# from random import shuffle
# import random as blabla

# print(
#     random
# )  # <module 'random' from 'C:\\Users\\gauri\\AppData\\Local\\Programs\\Python\\Python39\\lib\\random.py'>

# help(random)
# print(dir(random))
# print(random.random())  # random float bn 0 & 1
# print(random.randint(1, 9))  # random int within the range, limits inclusive
# print(random.choice([1, 3, 5, 7, 96, 4]))  # random from the given choice
# my_list = [1, 2, 3, 4, 5]
# random.shuffle(my_list)  # shuffles in place
# print(my_list)  # [1, 2, 4, 5, 3]


# import sys

# print(sys)  # <module 'sys' (built-in)>

# in the terminal- python module2.py Gauri Mhaiskar
# file = sys.argv[0]
# first = sys.argv[1]
# last = sys.argv[2]
# print(file, first, last)  # module2.py Gauri Mhaiskar

# EXTERNAL modules and packages - Python package index (PyPi) -- like NPM
# pip install <package name> in the command line.

# import pyjokes

# joke = pyjokes.get_joke("en", "neutral")
# print(joke)


# USEFUL MODULES
# specialized datatypes:
import collections
from typing import Counter, OrderedDict

# li = [1, 2, 3, 4, 5, 4, 3, 4, 5, 6, 7]
# print(Counter(li))  # Counter({4: 3, 3: 2, 5: 2, 1: 1, 2: 1, 6: 1, 7: 1})
# sentence = "bla bla bla.. thinking about python"
# print(
#     Counter(sentence)
# )  # Counter({' ': 5, 'b': 4, 'a': 4, 'l': 3, 't': 3, 'n': 3, '.': 2, 'h': 2, 'i': 2, 'o': 2, 'k': 1, 'g': 1, 'u': 1, 'p': 1, 'y': 1})

# di = {"a": 1, "b": 2}
# print(di["a"])
# print(di["c"])  # error.
# default dict allows us to access a key that doesnt exist but we can give it a default value.
# di2 = collections.defaultdict(lambda: 5, {"a": 1, "b": 2})
# # collections.defaultdict(callable func, dictionary )
# print(di2["c"])  # 5


# Dictionaries in Python3 are always ordered. so need this only for older versions
# di3 = OrderedDict()  # remembers the order in with elements were inserted
# di3["a"] = 1
# di3["b"] = 2

# di4 = OrderedDict()
# di4["a"] = 1
# di4["b"] = 2
# print(di3 == di4)  # True. because the order is same. would be False if order was diff.
# in a normal dictionary, as long as all keys and values match it results in True

import datetime

# print(datetime.date(2022, 1, 20))  # 2022-01-20
# print(datetime.time(5, 45, 2))  # 05:45:02
# print(datetime.date.today())

from array import array  # less memory performs faster than list.

arr = array("i", [1, 2, 3])  # array of integers.
print(arr[0])
