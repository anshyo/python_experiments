# question1

# n= int(input("till where you wanna take your numbers: "))
# a=0
# while a!=n:
#     a=a+1
#     print(a, end=" ")
# a=0
# b=a   
# while b!=n:
#     b=b+1
#     a=a+b
# print("\nsum of all those numbers are",a)
# print("average of all those numbers are",a/n)



# question2

# m=int(input("enter starting number: "))
# n=int(input("enter ending number: "))
# for i in range(m,n):
#     if i<=0:
#         pass
#     else:
#         print(i , end=" ")



# question3

# x= int(input("num: "))
# n= int(input("enter till where you wanna write your table:"))
# for m in range (1,n+1):
#     print(x,"x",m,"=",x*m)



# question4

# y= int(input("enter ,till where you wanna write your odd numbers: "))
# a=1
# while a<=y:
#     print(a , end=" ")
#     a=a+2



# question5

# n=int(input("enter, till where you wanna take your series: "))
# a=1
# b=0
# while a<=n:
#     b=b+1
#     print(a, end=" ")
#     a=a+b
#     c=a



# question6

# n=int(input("write your number: "))
# sum=0
# temp=n
# while temp>0:
#     digit=temp % 10
#     sum+=digit**3
#     temp//=10
# if n==sum:
#     print("its armstrong")
# else:
#     print("its not armstrong number")



# question7

# n=int(input("enter number: "))
# m=int(input("enter power: "))
# print("number raised is",(n**m)-n)



# question8

# n= int(input("till where you wanna take your natural number: "))
# a=0
# b=a
# while b!=n:
#     b=b+1
#     a=a+b
# print("sum of numbers is",a)



# question9

n=list((input("write numberin this format([2,3,4,5,6,7,8]): ")))
print("maximum number is" ,max(n))