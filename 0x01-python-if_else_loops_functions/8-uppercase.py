#!/usr/bin/python3
def uppercase(str):
    for i in str:
        i = ord(i)
        if ord(i) >= 97 and ord(i) <= 122:
            i = chr(ord(i) - 32)
            i = chr(i)
            print("{}".format(i), end="")
        print("")
