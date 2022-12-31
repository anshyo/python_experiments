import os
import etfunc

if __name__ == '__main__' :
    etfunc.welcome()

    os.system('rename mutableai.py\etfunc.py etfunc.txt')

    func_file = open('mutableai.py\etfunc.txt' , 'r')
    func_file_new = ''
    for lines in func_file:
        new_lines = ''
        if lines == "name = input('what is your name? : ')":
            new_lines += '#' + lines
        elif lines == "nameedit(f'name:{name};')":
            new_lines += '#' + lines
        elif lines == "a = f'hello {name} , i am cura'":
            data_file = open('mutableai.py\data.txt' , 'r')
            for data_line in data_file:
                data = data_line
            data_file.close()
            new_lines += lines.replace("{name}" , data[name])
        func_file_new += new_lines

    func_file.close()
    writing_file = open('mutableai.py\etfunc.txt' , 'w')
    writing_file.write(func_file_new)
    writing_file.close()

    os.system('rename mutableai.py\etfunc.txt etfunc.py')


