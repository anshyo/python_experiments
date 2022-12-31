import time

def nameedit(replace):
    func_file = open('mutableai.py\data.txt' , 'r')
    func_file_new = ''
    for lines in func_file:
        new_lines = lines.replace("1:1;" , replace)
        func_file_new += new_lines
    func_file.close()
    writing_file = open('mutableai.py\data.txt' , 'w')
    writing_file.write(func_file_new)
    writing_file.close()

def welcome():
    name = input('what is your name? : ')
    nameedit(f'name:{name};')
    a = f'hello {name} , i am cura'
    for i in a:
        print(i , end = '')
        time.sleep(0.1)