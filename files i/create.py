try:
    open('files i/test.txt' , 'x')
except FileExistsError:
    print('file exists')

a=0
x=0
while x!=10000:
    x=x+1
    y=(a+x)
    y=str(y)
    open('files i/text.txt' , 'a').write(y)
    open('files i/text.txt' , 'a').close()

    
