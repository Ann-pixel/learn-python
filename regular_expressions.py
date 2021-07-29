from functools import partial
import re

string = "search inside of this please! Adding this!"

# print(
#     "search" in string
# )  # True- this works too but reg-ex give us more searching powers


# print(
#     re.search("this", string)
# )  # <re.Match object; span=(17, 21), match='this'> -- a match object


# a = re.search("this", string)
# print(a.span())  # (17, 21) - start and stop as a tuple.
# print(a.start())  # 17
# print(a.end())  # 21
# print(a.group())  # this- part of the string that there was a match.


# pattern = re.compile("this")  # compile lets us make a pattern
# b = pattern.findall(string)
# print(b)  # ['this', 'this'] - piece of the string that matches in the form of a list

# c = pattern.fullmatch(string)
# print(c)  # None. full match means the pattern and string should match completely.

# d = pattern.match(string) #matches 0 or more chars from the beginning. does not care about indifferences after


# validating emails.
# email = "simba@dogs.com"
# pattern = re.compile(
#     r"([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
# )  # compile lets us make a pattern
# b = pattern.search(email)
# print(b)


# password- atlease 8 chars can contain letters symbols and $%#@.
# pattern = re.compile(r"[A-Za-z0-9@#$%]{8,}\d")
# psw = "Phoneix#78"
# a = pattern.fullsearch(psw)
# print(a)
