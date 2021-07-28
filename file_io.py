# my_file = open(
#     "text.txt"
# )  # open has a cursor concept. so next time we run open it will start at the last point it stopped
# print(
#     my_file.read()
# )  # Mr and Mrs Dursley of number four Private Drive were proud to say that they were perfectly normal, thank you very much!
# my_file.seek(0)  # moves the cursor back to 0
# print(my_file.read())


# readline reads each line one at a time
# my_file = open("text.txt")
# print(my_file.readline())  # Mr and Mrs...
# print(my_file.readline())  # :)
# print(my_file.readline())  # :)


# # close file once you re done reading it. so the cursor goes back.
# my_file.close()
# this is not recommended though--

# with statement is recommended--
# with open("text.txt", mode="r+") as my_file:  # mode: r+-read/write, w-write, r-read
#     print(my_file.read())
#     text = my_file.write("woooooohooooooo")
#     print(my_file.read())
#     print(text)


# with open("text.txt", "a") as my_file:  # append writes to the end
#     text = my_file.write("wooooohooooo")
# try:
#     with open("text.txt", "r") as my_file:  # append writes to the end
#         text = my_file.read()
#     print(text)
# except FileNotFoundError:
#     print("File not found")


# from translate import Translator

# with open("text.txt") as my_file:
#     fi = my_file.read()
#     translator = Translator(to_lang="hi")
#     tr_fi = translator.translate(fi)
#     with open("./text-hi.txt", mode="w") as my_file2:
#         my_file2.write(tr_fi)
