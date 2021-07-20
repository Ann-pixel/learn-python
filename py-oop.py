# class PlayerCharacter:
#     membership = True  # Class object attribute. it is defined outside of __init__. all instances have this attribute-True for everyone. this belongs to the class itself. unlike others, defined in the init func.- they belong to each respective instance.
#     # __init__ underscore is a dunder method. a constructor method.
#     def __init__(self, name="anonymus", age=0):  # self like 'this' in JS?
#         if age >= 18:
#             self.name = name
#             self.age = age

#     def run(self):
#         print(f"{self.name} is running!{self.membership} {PlayerCharacter.membership}")


# gauri = PlayerCharacter("Gauri", 14)
# gauri.run()
# print(gauri)
# ----EXERSICE!
# Given the below class:
# class Cat:
#     species = "mammal"

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age


# # 1 Instantiate the Cat object with 3 cats
# crookshanks = Cat("Crookshanks", 5)
# tabby = Cat("Tabby", 4)
# felix = Cat("Felix", 8)

# # 2 Create a function that finds the oldest cat
# cat_list = [crookshanks.age, tabby.age, felix.age]


# def find_max():
#     return max(cat_list)


# # 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2

# print(f"The oldest cat is {find_max()} years old.")


# DECORATOR---
# class Player:
#     def __init__(self, name, age):
#         self.name = name
#         self._age = age  # private variable.

#     def look(self):
#         return self

#     def shout(self):
#         print(f"My name is {self.name}.")

#     @classmethod  # cls is like self. class method is a method on the class. you dont need an instantiated object to use this. eg- Player.adding_things(2,4) is valid
#     def adding_things(cls, num1, num2):
#         return cls("Teddy", num1 + num2)  # instantiates a new player object.

#     @staticmethod  # no acces to 'cls'. used when we dont need the Class  in the method. accessible on class without instantiation.
#     def add_2(num):
#         return num + 2


# print(Player.add_2(3))
# # print(Player.adding_things(3, 4))  # -- 7
# # print(Player.adding_things(4, 6))
# # player2 = Player.adding_things(3, 6)
# # print(player2)
# simba = Player("Simba", 7)
# print(simba.look())
# simba.shout()
# print(simba.adding_things(3, 5))


# ----INHERITANCE


# class User:  # dont need __init if we're not defining any variables
#     def sign_in(self):
#         print("logged in")


# class Wizard(User):
#     def __init__(self, name, power):
#         self.name = name
#         self.power = power

#     def attack(self):
#         print(f"Attacking with {self.power}")


# class Archers(User):
#     def __init__(self, name, num_arrows):
#         self.name = name
#         self.num_arrows = num_arrows

#     def attack(self):
#         print(f"Attacking with {self.num_arrows} arrows.")


# wizard1 = Wizard("Gandalf", 50)
# # wizard1.sign_in()  # wizard inherits User.

# archer1 = Archers("Robin", 100)

# # wizard1.attack()
# # archer1.attack()

# print(isinstance(wizard1, Wizard))  # True
# print(isinstance(wizard1, User))  # True parent class
# print(isinstance(wizard1, object))  # True base class


# class User:
#     def __init__(self, email):
#         self.email = email

#     def sign_in(self):
#         print("logged in")


# class Wizard(User):
#     def __init__(self, name, power, email):
#         super().__init__(email)  # way to run the init method of the parent.
#         self.name = name
#         self.power = power

#     def attack(self):
#         print(f"Attacking with {self.power}")


# wizard1 = Wizard("Gandalf", 50, "gandalf@lotr.com")
# print(wizard1.email)  # gandalf@lotr.com
# print(
#     dir(wizard1)
# )  # introspection-  # tells us what kind object it is, what method it has etc.


# ----------DUNDER METHODS
# Py uses these methods to implement functions.
# eg __len__ is used to perform len(), __str__ is used in str() and so on.
# You can change the meaning of Dunder methods in classes in some cases. so the functions that come from those methods will change for instances of the class where the new meaning is defined.
# class Toy:
#     def __init__(self, color, age):
#         self.color = color
#         self.age = age

#     def __str__(
#         self,
#     ):  # we are redefining what __str__ means. so str(any instance of this class) will return its color.
#         return f"{self.color}"

#     def __call__(
#         self,
#     ):  # gives the ability to call a value like a func. eg action_figure()--#"Yes??"
#         return "Yes??"


# action_figure = Toy("red", 0)

# print(str(action_figure))  # red- changed meaning of str for this class.
# print(str(56))  #'56' #same meaning for everything else.
# print(action_figure())  # Yes?? because of __call__


# -----EXERSICE--
# class SuperList(list):
#     def __init__(self, this_list):
#         super().__init__(this_list)

#     def __len__(self):
#         return 200


# my_list1 = SuperList([1, 2, 3, 4])

# print(len(my_list1))
# print(my_list1)
# my_list1.append(5)
# print(my_list1)
# print(issubclass(SuperList, list))  # True

# --Multiple inheritances. pass in parents as args. call their individual inits in the child's init. have instances initaiate with all required parameters. assign appropriate parameters to respective parents' inits.

# MRO--- Method Resolution Order: Which methods to run in a complex inheritance


# class A:
#     num = 10


# class B(A):
#     pass


# class C(A):
#     num = 1


# class D(B, C):
#     pass


# print(D.num)  # 1 because it inherits from C
# # gives the Mro for precedence for D.
# print(
#     D.mro()
# )  # [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]


# --Exersice--
# class X:
#     pass


# class Y:
#     pass


# class Z:
#     pass


# class A(X, Y):
#     pass


# class B(Y, Z):
#     pass


# class M(B, A, Z):
#     pass


# print(M.mro())  # M_B_A_X_Y_Z
