from re import A
import re


def fact_rec(n):
    if n==1:
        return 1
    else:
        return n * fact_rec(n-1)



num=int(input('write integer:\n'))
print("your factorial is", fact_rec(num))