# print("Hello!")
# def func_hi():
#     print("hi there!")
# func_hi()
# EXERCISE!
# Display the image below to the right hand side where the 0 is going to be ' ', and the 1 is going to be '*'. This will reveal an image!
picture = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],
]
for item in picture:
    for bit in item:
        print("*" if bit else " ", end=" "),
    print(" ")


def multiply_by_2(num):
    return num * 2


def sum(num1, num2):
    return num1 + num2


name = input("What is your name!?")
activity = input("Whatchu doin?")
print(name + " is " + activity)
# -----FUNDAMENTAL DATA TYPES
# int  integer
# float floating point
# bool  Boolean
# str   "" String
# list  [] List- ordered sequence of objects
# tuple () List- but immutable.
# set   {} Unordered collections of unique objects.
# dict  {_:_} Dictionary- similar to hash tables in other languages.

# ------ CLASSES --> Custom types.

# ------ Specialized Data Types

# ------ None : absense of value.

# print(2+4)
# print(2*4)
# print(2-4)
# print(5/4)
# print(2 ** 3)
# print(5 // 4)
# print(5 % 4)
# MATH FUNCTIONS
# print(round(3.31))
# print(abs(-1))

# OPERATOR PRECEDENCE: PEMDAS
# () Perenthesis
# ** Exponents
# * /  Multiply, Divide. whichever comes first from left
# + - Add Subtract. whichever comes first from left

# print((5 + 4) * 10 / 2)  # 45.00

# print(((5 + 4) * 10) / 2) # 45.00

# print((5 + 4) * (10 / 2)) # 45.00

# print(5 + (4 * 10) / 2) # 25.00

# print(5 + 4 * 10 // 2) # 25

# a, b, c = 1, 2, 3
# print(a, b, c)

# augmented assignment operator
# some_value = 5
# some_value += 2
# print(some_value)

# some_str = "Hi there!"
# long_string = '''
# WOW
# O O
# ---
# '''
# print(long_string)
# first_name = "Gauri"
# last_name = "Mhaiskar"
# print(first_name+" " + last_name)

# ESCAPE SEQUENCE
# weather = "\t It\'s \n \"kind of\" sunny!"
# print(weather)


# FORMATTED STRING

# name = "Gauri"
# items = 10
# print(f"Hello there, {name}. You have {items} items")

# selfish ="01234567"

# string[start:stop:stepover]

# print(selfish[3]) #grab the specified idx //3
# print(selfish[1:6]) #span from 1st idx to the 6th- not including 6th. //12345
# print(selfish[1:8:2]) # stepover by 2 //1357
# print(selfish[:5:2])  # // 024
# print(selfish[2::2])  # // 246
# print(selfish[2:])    # // 234567
# print(selfish[-1])   #  negative idx means to start backwards // 7
# print(selfish[-3])  # // 5
# print(selfish[::-1]) # // 76543210

# ---Stirngs are immutable--
# can't assign selfish[1] = '9';

# # String methods
# quote = "to be or not to be"

# print(quote.upper()) #everything uppercase
# print(quote.capitalize()) #capitalize first letter
# print(quote.count("to"))  #count the occurances of "to"
# print(quote.find('or'))  #starting point of "or"
# print(quote.rjust(20))  #return a 20 char long right justified version of quote. ljust works similarly on the left.
# print(quote.replace("be", "me")) #replace all occurances of be with me

# name = "Gauri"
# is_cool = False
# is_cool = True
# print(bool(1))
# birth_year = input("What year were you born? ")
# age = 2021 - int(birth_year)
# print(f"Your are {age} years old.")

# PASSWORD CHECK
# name = input("Enter your username? ")
# psw = input("Enter your passoword? ")
# print(f"{name}, your password {'*'* len(psw)} is {len(psw)} characters long.")


# ---------LIST - data structure
# ordered sequence of objects-- a type of Array.
# li = [1,2,3,4]
# li2= ["a", "b", "c"]
# li3 = [1,2,'a', True, 5.5]
# amazon_cart=["notebooks", "sunglasses"]
# print(amazon_cart[0])
# List slicing works like string slicing
# amazon_cart = ["notebooks", "sunglasses", "toys", "grapes","books"]
# print(amazon_cart[2])
# print(amazon_cart[1:3:1])
# print(amazon_cart[2:4:2])
# print(amazon_cart[0::2])
# amazon_cart[0] = "video games" # lists are mutable
# print(amazon_cart)
# print(amazon_cart[0:3])  #slicing creates a new list. does not mutate the original list

# reference data type: py-lists work like JS-objects here
# new_cart = amazon_cart # straight assignment points to the place of the list in memory.
# new_cart1 = amazon_cart[:] #this makes a new copy and new_cart1 points to that new copy not the original ---like {...amazon_cart} or Object.assign(amazon_cart) in JS
# new_cart1[0] ="gum"
# print(amazon_cart)

# Matrix -- a concept that is used in multiple languages. 2D arrays.
# used in image-processing..etc
# matrix = [
#   [1,2,3],
#   [2,4,6],
#   [7,8,9]
# ]
# print(matrix[2][2]) # //9


# List Methods---
# basket = [1,2,3,4,5]
# print(len(basket))
# basket.append((100))
# print(basket)
# new_list = basket.append(200)  # append changes the list in place. and cant be assigned to anything new
# print(new_list) #//-None
# basket.insert(3, 100) #insert also modifies list in place
# print(basket)
# basket.extend([101,102,103]) #  inserts an iterable. also modiies in place
# # basket.extend([1000]) #---also valid
# print(basket)  #[1,2,3,100,4,5,101,102,103]

# basket = [1,2,3,4,5]
# popped = basket.pop() # remove the last one  and returns its value
# print(basket, popped) # [1,2,3,4], 5
# popped1 = basket.pop(3)
# print(basket, popped1) #[1,2,3] 4  //pops a specific index

# rem = basket.remove(3)  # removes a specified value in place. no assignment. rem=None.
# print(basket, rem)  # [1,2,4] None

# basket.clear() # clears the list in place.
# print(basket) # //- []

# basket = ['a','b','c','d','e']
# print(basket.index("a")) # returns index of specified value
# print(basket.index("d", 0, 4)) # returns index of specified value within specified range. if not in the range- throws an error.
# #to avoid errors. check with 'in' first.
# print("d" in basket) #//True
# print(basket.count("d"))
# basket.sort() #sorts in place.
# basket.reverse()  # reversees in place. doesnt return anything.
# print(basket) # // edcba
# print(basket[::-1]) # returns the reversed string. does not change the original.

# range_from_list = list(range(1,100))  #create a quick list. 1-->99
# print(range_from_list)

# range2_from_list = list(range(100)) #creates a list from 0--> 99
# print(range2_from_list)

# sentence ="!"
# new_sentence = sentence.join(["hi", "i'm", "shark"]) #join returns a new string. #hi!i'm!shark
# print(new_sentence)

# new_sentence2= " ".join(["hi", "i'm", "shark"]) # hi i'm shark
# print(new_sentence2)

# LIST UNPACKING = destructuring in JS

# a, b, c = [1,2,3]
# print(a) #1
# print(b) #2
# print(c) #3

# a,b,c,*others = [1,2,3,4,5,6,7,8]
# print(a,b,c,others)  #// 1 2 3 [4, 5, 6, 7, 8]

# a,b,c,*others,d = [1,2,3,4,5,6,7,8]
# print(a,b,c,others, d)  #// 1 2 3 [4, 5, 6, 7] 8

# ----NONE
# None is absense of value. like null in JS
# a= None
# print(a) #// None
# print(bool(None)) #//False


# ----DICTIONARY--- like hash tables in other languages. == Key Value pairs. Unordered
# keys can be anything immutable. strings, bool, numbers not lists coz lists are mutable.
# user = {
#   "basket": [1,2,3],
#   "greet": "hello"
# }

# print(user["age"]) # if it doesnt exist. it throws an error. so use .get() instead

# print(user.get('age')) # returns None if it doesnt exist.
# print("basket" in user) # //True. only checks for keys.
# print(user.get('age', 55)) # if you want to add a default value if no value exists // returns 55. does not change the original dictionary.
# # print(user) # still logs {"basket: ..., "greet":....} -- no "age"
# print(user.get("greet", "hi")) # greet already exists, so it doesnt get the default val. returns "hello"

# # another way to create a dictionary
# user2 = dict(name= "Shark")
# print(user2) # //- {"name": "Shark"}

# print(user.keys()) # returns an array of  all keys // dict_keys(["bakset", "greet"])
# print("greet" in user.keys()) #True

# print(user.values()) #returns array of values // dict_values([[1,2,3], "hello"])
# print("hello" in user.values()) #//True


# print(user.items()) #-- dict_items([("basket", [1,2,3]), ("greet", "hello")]). this is an array of tuples.

# print(user.clear()) # //None- clears the dictionary in place and returns nothing.

# user.clear() #clears the dictionary
# print(user)  # // {} --user is now empty.

# copying dictionary does not work like JS objects. ie: is not a reference type.
# user2 = user.copy()
# print(user2)
# user2["age"] = 55
# print(user2, user)   # user2 contains "age". user still does not.

# print(user2.pop("age")) # removes the value and returns it.and
# print(user2) #age doesnt exist here anymore.

# user2.popitem() # randomly removes any key val pair

# user.update({"greet": "Hi!"}) # updates value of an existing key. adds a value for a key that doesnt exits.
# print(user)


# -------TUPLE :: like Lists but immutable. everything else like lists. faster.
# cant sort or reverse a tuple because of immutablity.
# cant perform any "in-place" actions that may change it.

# my_tuple = (1,2,3,4,5)
# my_tuple[1] ="z"  #this would throw an error.

# print(my_tuple[1]) #--2
# print(4 in my_tuple) #True.

# dictionary.items() will return an array of key-val pairs in a tuple.
# new_tuple = my_tuple[1:2]
# # print(new_tuple) #-- (2,) a tuple with a single item wil have a ',' at the end.
# new_tuple2 = my_tuple[1:4]
# print(new_tuple2) # (2,3,4)

# x= my_tuple[0]
# print(x)

# x,y,z, *other = my_tuple
# print(x,y,z,other) # 1 2 3 [4,5]

# print(my_tuple.count(5)) # -- 1
# print(my_tuple.index(5)) #-- 4
# print(len(my_tuple)) # -- 5

# --------SETS-----------
# no duplicate values . no indices. because it is unordered.
# my_set = {1,2,3,4,5}
# print(my_set)
# my_set.add(100)
# my_set.add(2)
# print(my_set) #-- {1,2,3,4,5,100} -- 2 doesnt get added coz its not unique.

# my_list = [1,2,3,4,5,5]
# create_set = set(my_list)
# print(create_set)  # --- {1,2,3,4,5}

# print(my_set[3]) #-- Error. coz no idices.
# print(3 in my_set) # -- True
# print(len(my_set)) #-- 5

# not a reference type. if set is changed after copying. new set still keeps its value.
# new_set = my_set.copy()
# print(new_set)
# my_set.clear()
# print(new_set, my_set)  #-- {1,2,3,4,5} set()

# my_set =  {1,2,3,4,5}
# your_set = {4,5,6,7,8,9,10}
# print(my_set.difference(your_set)) # what does my_set have that your_set does not == {1,2,3}

# my_set.discard(5)  # removes an item in place, if present. returns None.
# print(my_set)  # {1,2,3,4}

# my_set.difference_update(your_set) #removes elements of your_set from my_set in place. returns nothing
# print(my_set)  # {1,2,3}

# print(my_set.intersection(your_set)) #returns common items in both {4,5}
# print(my_set & your_set) #returns common items in both {4,5} shorthand for intersection

# print(my_set.isdisjoint(your_set)) # --False. returns True if the 2 sets have nothing in common.

# print(my_set.issubset(your_set)) # True if my_set is a subset of your_set. in this eg. it returns False. if my_set = {4,5} that would return True.

# print(my_set.issuperset()) # True if my_set is a superset(it encompasses) your_set. in this eg: False.

# print(my_set.union(your_set)) # combines both sets to give a new set. so no duplicate values. {1,2,3,4,5,6,7,8,9,10}

# print(my_set | your_set) # shorthand for .union method


# is_old = True
# is_licenced = True
# if is_old and is_licenced:
#     print("You may drive.")
# else:
#     print("You are not allowed to drive.")

# TRUTHY FALSY values
# greet = "hello"
# num = 5
# num_false = 0
# str_false = ""
# print(bool(greet), bool(num)) #True True. any value will resolve to Truthy.
# print(bool(num_false), bool(None), bool(str_false)) #False False False. None and 0 and empty str resolve to false.  So do any empty data str: list, tuple, set, dictionary

# TERNARY OPERATORS / CONDITIONAL EXPRESSION
# condition_if_true if condition else condition_else
# do_this_if_true if check_this_condition_first else do_this_if_false.
# is_friend = True
# can_message = "You may message your friend!" if is_friend else "You cant message someone who is not your friend."
# print(can_message) #"You may message your friend"

# SHORT CIRCUITING
# for 'and' if the first value is False, the second value doesnt get evaluated. it shortcircuits to the next action.
# for 'or' if the first value is True, the second value doesnt get evaluated. it shortcircuits to the next action.

# LOGICAL OPERATORS
# < > == <= >= != or and not

# a stupid challenge
# is_magician = False
# is_expert = False
# print("You are a magician! good job!" if is_magician else "You need to be a magician")
# if is_expert and is_magician:
#   print("You are a master magician")
# elif not is_expert and is_magician:
#   print("You are not  an expert. but you are getting there!")


# IS VS ==
# == checks for actual value.
# print(True == 1)    #true
# print("" == 1)      #false
# print([]==1)        #false
# print(10 == 10.0)   #true
# print([] == [])     #true


# IS checks if the location in memory is the same.
# print(True is 1)    #false
# print("" is 1)      #false
# print([] is 1)      #false
# print(10 is 10.0)   #false
# print([] is [])     #false

# FOR LOOP:
# for item in 'Gauri Mhaiskar':
#   print(item)

# for item in [1,2,3,4,5]:
#   print(item * 2) #246810

# for item in {6,7,8,9}:
#   print(item ) #8967--- unordered

# for item in (11,12,13,14):
#   print(item) #11 12 13 14

# iterable : list, tuple, dictionary, set, string, range

# user = {
#   'name': "Dumbledore",
#   'age' : 110,
#   'likes_bertiebots': False
# }

# for item in user:
#   print(item) #name \n age \n likes_bertiebots

# for item in user.items():
#   print(item) #('name', 'Dumbledore')\n('age', 110)\n('likes_bertiebots', False)

# for item in user.keys():
#   print(item) #name \n age \n likes_bertiebots

# for item in user.values():
#   print(item) #Dumbledore \n 110 \n False

# for key,value in user.items():
#   print(f"key: {key}, value: {value}")

# key: name, value: Dumbledore
# key: age, value: 110
# key: likes_bertiebots, value: False


# COUNTER EXERSISE
# my_list = [1,2,3,4,5,6,7,8,9,10]
# count = 0
# for num in my_list:
#   count += num
# print(f"total of my_list is: {count}")


# RANGE-- data obj.

# range(start, stop, stepover)

# my_range = range(10)
# for num in my_range:
#   print(num) # 0123456789

# your_range = range(1,10)
# for num in your_range:
#   print(num) #123456789

# your_range = range(1,10)
# for _ in your_range:
#   print("_ means dummy variable") #123456789

# ENUMERATE: gives index + value of in iterable in a tuple
# (0, 'H')
# (1, 'e')
# (2, 'l')
# (3, 'l')
# (4, 'o')
# for char in enumerate("Hello"):
#   print(char)

# 0 is G
# 1 is a
# 2 is u
# 3 is r
# 4 is i
# for idx, val in enumerate("Gauri"):
#   print(f"{idx} is {val}")
# small challenge---
# for idx, val in enumerate(list(range(100))):
#   if val == 50:
#     print(f"idx of 50 is: {idx}")


# WHILE LOOP
# i = 0
# while i<10:
#   print(i)
#   i+=1
#   break
# else:
#   print("done with all work!")

# USE CASE for WHILE
# while True:
#   response= input("Say something: ")
#   if(response =="bye"):
#     break

#'continue': is used in loops to get back to the enclosing loop. so lines after the word dont get executed
#'pass' means, go to the next line. doesnt do anything. can be used as placeholder code.


# EXERCISE!
# Display the image below to the right hand side where the 0 is going to be ' ', and the 1 is going to be '*'. This will reveal an image!
# picture = [
#   [0,0,0,1,0,0,0],
#   [0,0,1,1,1,0,0],
#   [0,1,1,1,1,1,0],
#   [1,1,1,1,1,1,1],
#   [0,0,0,1,0,0,0],
#   [0,0,0,1,0,0,0]
# ]
# for item in picture:
#   for bit in item:
#     print("*" if bit else " ", end=" "),
#   print("")

# EXERCISE - find and print dupes in a list
# some_list = ["a","b","c","b","d","m","n","n"]
# some_dict = {}
# for letter in some_list:
#   if letter in some_dict:
#     some_dict[letter] +=1
#   else:
#     some_dict[letter] =1
# for letter in some_dict:
#   if some_dict[letter] ==2:
#     print (letter, end =" ")

# # another BETTER solution!
# duplicates =[]
# for value in some_list:
#   if some_list.count(value) > 1 and value not in duplicates:
#     duplicates.append(value)
# print(duplicates)


# FUNCTIONS

# def say_hello(greet):
#   print(greet)
# say_hello("BOOYAH!")
# def show_tree():
#   picture = [
#   [0,0,0,1,0,0,0],
#   [0,0,1,1,1,0,0],
#   [0,1,1,1,1,1,0],
#   [1,1,1,1,1,1,1],
#   [0,0,0,1,0,0,0],
#   [0,0,0,1,0,0,0]
#   ]
#   for item in picture:
#     for bit in item:
#       print("*" if bit else " ", end=" "),
#     print("")

# show_tree()
# show_tree()

# positional parameters when we define
# def greet(name, emoji):
#   print(f"Hi there, {name}! {emoji}")
# # #positional arguments when we call
# # greet("Gauri", '🎈')
# #keyword arguments
# greet(emoji="😊", name="Satya")

# def add(n1, n2):
#   return n1 + n2

# print(add(4,5))


# TESLA EXERCISE
# def checkDriverAge(age = 0):
#   # age = input("What is your age?: ")
#   if int(age) < 18:
# 	  print("Sorry, you are too young to drive this car. Powering off")
#   elif int(age) > 18:
# 	  print("Powering On. Enjoy the ride!");
#   elif int(age) == 18:
# 	  print("Congratulations on your first year of driving. Enjoy the ride!")
# checkDriverAge()

# Methods and functions. functions are global. methods are owned. eg. the .capitalize() method belongs to String.


# Docstring-- add comments/definitions to functions so that the ide/editor understands.
# def say_hi(name):
#   '''
#   info: this function prints a greeting for the user!
#   '''
#   print(f"hi {name}")

# say_hi("simba")

# help(say_hi)

# print(say_hi.__doc__)

# def odd_even(num):
#   return num % 2 == 0
# print(odd_even(4))


# *args **kwargs
# RULE FOR DEFINING FUNC PARAMETERS: params, *args, default parameters, **kwargs
# def super_func(*args, **kwargs):
#   print(args)  #(1, 2, 3, 4, 5) - tuple
#   print(kwargs) #{'num1': 3, 'num2': 10} - dictonary
#   return sum(args)

# print(super_func(1,2,3,4,5, num1=3, num2 = 10)) #15


# EXERSICE- HIGHEST EVEN
# def highest_even(my_list):
#   even_num = my_list[0]
#   for num in my_list:
#     if num % 2 ==0 and num > even_num:
#       even_num = num
#   return even_num if even_num % 2 == 0 else -1

# def highest_even1(my_list):
#   evens = []
#   for num in my_list:
#     if num %2 ==0:
#       evens.append(num)
#   return max(evens)

# print(highest_even([1,3,11,5]))


# a= "hey ohhhhhhh!"

# if (n:= len(a)) > 7:
#   print(f"too long! {n} char long")


# while (n := len(a)) >1:
#   print(n, a)
#   a= a[:-1]

# SCOPE- is only created in a new function.
# a= 1
# def confusion():
#   a=5
#   return a
# print(a)                # 1
# print(confusion())      # 5
# print(a)                # 1


# Start in local env. then step to parent..and so on..to global then to built-in python functions.
# total=0
# def count():
#   global total
#   total += 1
#   return total

# print(count())


# def outer():
#   x = "local"
#   def inner():
#     nonlocal x
#     x = "non local"
#     print("inner: ", x) # "nonlocal"
#   inner()
#   print("outer: ", x)  #"nonlocal"

# outer()

# if 5>2: print("yes!")

# print("YEs" if 5 > 2 else "NO")

# print("Yes") if 5 > 2 else print("No")
