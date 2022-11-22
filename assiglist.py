# ques1

# l = [1,3,4]
# print(sum(l))



# ques2

# l = [1,4,5]
# b = 1
# for i in l:
#     b *= i
# print(b)



# ques3

# l = [1,3,4]
# print(max(l))



# ques4

# l = [1,3,4]
# print(min(l))



# ques5

# l = (input("enter elements separated with commas: "))
# l = l.split(",")
# c = 0
# for i in l:
#     if i[0] == i[-1] and len(i) >= 2:
#         c += 0
# print(c)



# ques6

# a = [(2,1) , (1,2) , (2,5) , (4,4) , (2,3)]
# e = []
# for i in a:
#     x = []
#     x.append(i[-1])
#     m = i[0:len(i)-1]
#     x += m
#     e.append((x))
# e = sorted(e)
# f = []
# for i in e:
#     x = []
#     x.append(i[-1])
#     m = i[0:len(i)-1]
#     x += m
#     f.append(tuple(x))
# print(f)


# ques 7

# a = [1,2,34,34,34,5,456,456,67,8768,7,8,87,7,6,4,2,6]
# b = []
# d = True
# while True:
#     i = a[0]
#     for j in b:
#         if j == i:
#             d = False
#     if d:
#         b.append(i)
#     a.pop(0)
#     d = True
#     if len(a) == 0:
#         break
# print(b)




# ques8

# l = eval(input("list: "))
# if len[l] == 0:
#     print("it is emplty")
# else:
#     print("it is not emplty")



# ques9

# a = eval(input("list: "))
# b = a




# ques10

# a = eval(input("list: "))
# n = 3
# for i in a:
#     if len(i) > n:
#         print(i)




# Ques11

# a = [1,2,3,4,5]
# b = [5,6,7,8,9]
# c = True
# if len(b) > len(a):
#     a , b = b , a
# while True:
#     i = a[0]
#     for j in b:
#         if i == j:
#             c = False
#     a.pop(0)
#     if len(a) == 0:
#         break
# print(c) 




# ques12

# a = eval(input('list: '))
# a.pop(0)
# a.pop(3)
# a.pop(3)





# ques 14

# a = eval(input("list: "))
# for i in a:
#     try:
#         if 2 % i == 0:
#             a.remove(i)
#     except:
#         pass
# print(a)




# ques15

# import random

# a = [1,443,5,54,56,65,56,65,65,655,5]
# b = []
# c = 0 
# d = []
# for i in a:
#     b.append(c)
#     c += 1
# while len(b) != 0:
#     e = random.choice(b)
#     d.append(a[e])
#     b.pop(b.index(e))
# print(d)




# ques16

# a = []
# for i in range(31):
#     a.append(i**2)
# print(a[0:6])
# print(a[-5:31])





# ques17

# a = []
# for i in range(31):
#     a.append(i**2)
# print(a[6:31])





# list input

d = {}
while True:
    m = input("Enter employment salary with space(if not , enter 'n' or 'N'): ")
    m = m.split(" ")
    d[m[0]] = m[1]
    x = input("want to add more?(Y/N) : ")
    if "N" or "n" in x:
        break
    else:
        continue
print(d)
