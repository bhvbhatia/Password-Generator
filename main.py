# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import random
passlen = int(input("Enter the Length of Password: "))
words = "abcdefghijklmnopqstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123467890!@#$^&*()?"
pas = "".join(random.sample(words, passlen ))
print(pas)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
