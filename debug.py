# linting
# ide/editors
# reading errors
# PDB - Python Debugger. a built-in module.

import pdb


def add(num1, num2):
    pdb.set_trace()  # pdb in the terminal. hit help to get a list of possible commands
    t = 4 + 5

    return num1 + num2


add(4, "asdhf")
