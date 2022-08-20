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

# lisT=[]
# n=int(input("how many numbers should be in your list: "))
# print("numns: ",end='')
# for i in range(0,n):
#     num=int(input())
#     lisT.append(num)   
# lis=lisT
# print("maximum number is",lis)



# question10

# n=int(input("enter your number: "))
# sum=0
# while n!=0:
#     dig=n%10
#     sum=sum+dig
#     n=n//10
# print("sum of all digits in number is",sum)



# question11

# num= int(input("enter a number:"))
# f=False
# if num>1:
#     for i in range(2,num):
#         if num%i==0:
#             f=True
#             break
# if f:
#     print("numbers is not primenumber")
# else:
#     print("number is prime number")



# question12

# n=int(input("enter your number: "))
# print("your reversed idgit is",end=" ")
# while n!=0:
#     dig=n%10
#     print(dig,end='')
#     n=n//10



# question13

# n=int(input("enter your number: "))
# m=n
# reverse=0
# while n!=0:
#     dig=n%10
#     reverse= reverse*10+dig
#     n=n//10
# print(reverse)
# if reverse==m:
#     print("its a palindrome")
# else:
#     print("its not a palindrome")



# question14

# n=int(input("time where you wanna take your fabonacci table: "))
# a=0
# b=1
# c=1
# print(a,end=" ")
# while c<=n:
#     print(c, end=" ")
#     c=a+b
#     a=b
#     b=c



# question15

# yet to do



# question16

# n= int(input("write a number(positive): "))
# b=0
# while b!=n:
#     b=b+1
#     print('* '*b)



# question17

# n= int(input("write a number(positive): "))
# while n!=0:
#     print('* '*n)
#     n=n-1



# question18

# yet to be done



# question19

for j in range(1,101):
    for i in range(2,j):
        if j%i==0:
            pass
        else:
            print(i)