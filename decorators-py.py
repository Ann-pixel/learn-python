# DECORATORS.
# functions in py are first class citizens.
# they act like variables. they are resolved to a value and can be passed around in other functions.
# decorators can be used to add extra features to functions.
# HOF- func that accepts or returns another func.

# Decorator


# def my_deorator(func):
#     def wrap_func(*args, **kwargs):
#         print("********")
#         func(*args, **kwargs)
#         print("********")

#     return wrap_func


# @my_deorator
# def hello(greeting, emoji="🎃"):
#     print(greeting, emoji)


# hello("hi there!")


# EXERSICE performance decorator.
# from time import time


# def performance_decorator(func):
#     def wrapper(*args, **kwargs):
#         t1 = time()
#         func()
#         t2 = time()
#         print(f"time to run the function is: {t2-t1} s")

#     return wrapper


# @performance_decorator
# def long_time():
#     for i in range(10000):
#         i * 5
#     return True


# long_time()  # time to run the function is: 0.0029904842376708984 ms


# Create an @authenticated decorator that only allows the function to run is user1 has 'valid' set to True:
user1 = {
    "name": "Sorna",
    "valid": False,  # changing this will either run or not run the message_friends function.
}


def authenticated(fn):
    def wrapper(*args, **kwargs):
        if args[0]["valid"]:
            return fn(*args, **kwargs)
        print("Thou shall not pass!!!")

    return wrapper


@authenticated
def message_friends(user):
    print("message has been sent")


message_friends(user1)
