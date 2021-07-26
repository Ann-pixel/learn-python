# range(100)- doesnt live in memory. that is a generator.
# generates values one at a time.

# eg- list, dict, set etc are iterables that live in memory.
# is in the function below. a generator func uses a 'yeild' keyword instead of return to give/return one value at a time w/o stopping the function


# def generator_function(num):
#     for i in range(num):
#         yield i  # yeild key word pauses the function. next() resumes it.


# yeild keyword tells py that it is a generator function.
# only stores the recent value in memory. not all of it..

# for item in generator_function(50):
#     print(item)

# g = generator_function(20)
# next(g)
# next(g)
# print(next(g))  # 2


# how for works under the hood.
# def special_for(iterable):
#     iterator = iter(iterable)
#     while True:
#         try:
#             print(iterator)
#             next(iterator)
#         except StopIteration:
#             break


# special_for([1, 2, 3, 4])

# <list_iterator object at 0x0000017580D23FD0>
# <list_iterator object at 0x0000017580D23FD0>
# <list_iterator object at 0x0000017580D23FD0>
# <list_iterator object at 0x0000017580D23FD0>
# <list_iterator object at 0x0000017580D23FD0>


# creating our own Range func:


# class My_Gen:
#     current = 0

#     def __init__(self, first, last):
#         self.first = first
#         self.last = last

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if My_Gen.current < self.last:
#             num = My_Gen.current
#             My_Gen.current += 1
#             return num
#         raise StopIteration


# gen = My_Gen(0, 10)
# for i in gen:
#     print(i)

# FIBONACCI
# def fib(num):
#     a = 0
#     b = 1
#     for i in range(num):
#         yield a
#         temp = a
#         a = b
#         b = temp + b


# for x in fib(5): #for calls the iterator in the generator func.
#     print(x)
