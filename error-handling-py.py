# while True:
#     try:  # try this
#         age = int(input("enter your age."))
#         print(age)
#     # except:  # execute this if 'try' throws an error
#     #     print("Age must be a number.")
#     except ValueError:  # execute this if 'try' throws a Value error
#         print("Age must be a number.")
#     except ZeroDivisionError:  # execute this if 'try' throws a zero division error
#         print("Age must be a number.")
#     else:  # do this if all runs smoothly
#         print("Thanks!")
#         break


# def add(num1, num2):
#     try:
#         return num1 / num2
#     # except TypeError as err:
#     #     print(f"Something is wrong.---- {err}")
#     except (TypeError, ZeroDivisionError) as err:
#         print(f"oops {err}")


# print(add(1, "3"))
# print(add(1, 0))


while True:
    try:  # try this
        age = int(input("enter your age."))
        print(age)
        # raise ValueError("HEY! cut it out!")  #throw your own error
        # raise Exception("HEY! cut it out!")  #throw your own error
    # except:  # execute this if 'try' throws an error
    #     print("Age must be a number.")
    except ValueError:  # execute this if 'try' throws a Value error
        print("Age must be a number.")
    except ZeroDivisionError:  # execute this if 'try' throws a zero division error
        print("Age must be a number.")
    else:  # do this if all runs smoothly
        print("Thanks!")
        break
    finally:  # run after everything-regardless of err/no err.
        print("Done!")
