# pure functions- given same input always gives out the same output. does not have any side-effects.
from typing import SupportsComplex


def multiply_by_2(li):
    new_li = []
    for item in li:
        new_li.append(item * 2)
    return new_li


# # this func is a pure func. same op for same ip. no side effects.
# print(multiply_by_2([1, 2, 3, 4]))

# MAP FILTER ZIP REDUCE.
# map(func(action), iterable(to perform action on))
# print(map(multiply_by_2, [1, 2, 3]))  # -<map object at 0x000002556E3EFCD0>
# print(list(map(multiply_by_2, [1, 2, 3])))
# ERR_ int object is not iterable. no need to create a seperate new list.
# def multiply_by_2_for_map(item):
#     return item * 2


# # map returns a map object. so we convert it to list first. creates a new list. like in JS.
# print(list(map(multiply_by_2_for_map, [1, 2, 3])))

# FILTER- adds to the new list if func resolves True for each item in list.
# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]


# def check_odd(item):
#     return item % 2 != 0


# filtered_list = filter(check_odd, my_list)
# print(list(filtered_list))  # [1, 3, 5, 7, 9]


# ZIP- zip two or more (ordered or unordered) iterables(list, tuple, set, dict) together. return a list of tuples joined at the common indices.
# my_list = {1, 2, 3}
# my_dict = {"a": 1, "b": 2, "c": 3}
# your_list = [10, 20, 30]
# uneven_list1 = [1, 2, 3, 4, 5]
# uneven_list2 = [1, 2, 3]

# print(list(zip(my_list, your_list)))  # [(1, 10), (2, 20), (3, 30)]
# print(list(zip(my_list, your_list, my_list)))  # [(1, 10, 1), (2, 20, 2), (3, 30, 3)]
# print(list(zip(uneven_list1, uneven_list2)))  # [(1, 1), (2, 2), (3, 3)]
# print(list(zip(my_list, my_dict)))  # [(1, 'a'), (2, 'b'), (3, 'c')]
# print(list(zip(my_list, my_dict.values())))  # [(1, 1), (2, 2), (3, 3)]
# print(list(zip(my_list, my_dict.keys())))  # [(1, 'a'), (2, 'b'), (3, 'c')]
# print(
#     list(zip(my_list, my_dict.items()))
# )  # [(1, ('a', 1)), (2, ('b', 2)), (3, ('c', 3))]

# REDUCE- not a Py built in func. so we import from 'functools'
# from functools import reduce

# reduce(reducer-func, iterable, inital-value-for-accumulator)
# my_list = [1, 2, 3]


# def reducer_func(acc, item):
#     print(acc, item)
#     return acc + item


# print(reduce(reducer_func, my_list, 0))
# 0 1
# 1 2
# 3 3
# 6

# EXERSICE--
# from functools import reduce

# 1 Capitalize all of the pet names and print the list
# my_pets = ["sisi", "bibi", "titi", "carla"]
# def map_my_pets(pet):
#     return pet.capitalize()
# print(list(map(map_my_pets, my_pets)))  # ['Sisi', 'Bibi', 'Titi', 'Carla']

# 2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
# my_strings = ["a", "b", "c", "d", "e"]
# my_numbers = [5, 4, 3, 2, 1]

# print(
#     list(zip(my_strings, sorted(my_numbers)))
# )  # [('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5)]

# 3 Filter the scores that pass over 50%
# scores = [73, 20, 65, 19, 76, 100, 88]
# def filter_func(score):
#     return score > 50
# print(list(filter(filter_func, scores)))  # [73, 65, 76, 100, 88]

# 4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?
# def reduce_func(acc, item):
#     return acc + item
# scores.extend(my_numbers)
# print(reduce(reduce_func, (my_numbers + scores), 0))  # 456


# LAMBDA EXPRESSIONS!- anonymous-onetime functions. arrow func in JS

# lambda param: action-using param

# my_list = [1, 2, 3, 4, 5]
# your_list = map(lambda item: item * 2, my_list)

# print(your_list)  # <map object at 0x00000110EFEE3DC0>
# print(list(your_list))  # [2, 4, 6, 8, 10]


# EXERSICE>
# 1 one line func that gives a squared list.
# my_list = [5, 4, 3]

# print(list(map(lambda item: item ** 2, my_list)))  # [25, 16, 9]

# 2 List sorting -  sort list based on each of the second value in tuple.
# a = [(0, 2), (4, 3), (9, 9), (10, -1)]
# a.sort(key=lambda val: val[1])
# print(a)  # [(10, -1), (0, 2), (4, 3), (9, 9)]


# COMPREHENSIONS - list, dict ,set.
# way to quickly create objects.
# one way to make a list.
# my_list = []
# for char in "hello":
#     my_list.append(char)
# print(my_list)  # ['h', 'e', 'l', 'l', 'o']

# using comprehensions.--- my_list = [param for param in iterable]
# my_list = [char for char in "hello"]
# print(my_list)  # ['h', 'e', 'l', 'l', 'o']
# my_list2 = list(range(0, 100))
# print(my_list2)
# my_list3 = [num for num in range(0, 100)]
# my_list4 = [num * 2 for num in range(0, 100)]
# print(my_list4)

# get even numbers.
# my_list5 = [num ** 2 for num in range(0, 100) if num % 2 == 0]
# print(my_list5)

# my_set = {num for num in range(0, 10)}
# print(my_set)  # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

# my_dict = {key: value for (key, value) in iterable}
# simple_dict = {"a": 1, "b": 2}
# my_dict = {key: value ** 2 for key, value in simple_dict.items()}
# print(my_dict)  # {'a': 1, 'b': 4}

# my_dict = {num: num * 2 for num in [1, 2, 3, 4]}
# print(my_dict)  # {1: 2, 2: 4, 3: 6, 4: 8}

# EXERSICE--
# some_list = [char for char in "abcdeace"]
# duplicates = list({char for char in some_list if some_list.count(char) > 1})
# print(duplicates)  # ['a', 'c', 'e']
