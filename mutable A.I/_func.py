import main

data_list = {}
name = ''
def func_editor(changing , change):
    func_content = ''
    func_file = open('mutable A.I\_func.py' , 'r')
    c = 0
    for line in func_file:
        if changing in line:
            if c == 1:
                break
            func_content += line.replace(changing , change)
            c += 1
        else:
            func_content += line
    func_file.close()
    func_file = open('mutable A.I\_func.py' , 'w')
    func_file.write(func_content)
    func_file.close() 

def func_commenter(start):
    func_content = ''
    func_file = open('mutable A.I\_func.py' , 'r')
    for line in func_file:
        if start in line:
            pass
        else:
            func_content += line
    func_file.close()
    func_file = open('mutable A.I\_func.py' , 'w')
    func_file.write(func_content)
    func_file.close() 

def reset():
    reset_file = open('mutable A.I\_reset.txt' , 'r')
    reset_content = ''
    for line in reset_file:
        reset_content += line
    reset_file.close()
    reset_file1 = open('mutable A.I\_func.txt' , 'w')
    reset_file1.write(reset_content) 
    reset_file1.close()

def reset_file_writer():
    func_content = ''
    func_file = open('mutable A.I\_func.py' , 'r')
    for line in func_file:
        func_content += line
    func_file.close()
    func_file1 = open('mutable A.I\_reset.txt' , 'w')
    func_file1.write(func_content)
    func_file1.close() 

# def func_line_insert():


def commenter_line_saver():
    func_content = ''
    func_file = open('mutable A.I\_func.py' , 'r')
    alphas = 'qwertyuioplkjhgfdsazxcvbnm'
    for line in func_file:
        if 'func_commenter' in line:
            c = 0
            first_letter = ''
            for i in line:
                if i in alphas:
                    if c == 4:
                        break
                    c += 1
                    first_letter += i
            if first_letter == 'func':
                func_content += line
    func_file.close()
    func_file = open('mutable A.I\commenter_lines.txt' , 'w')
    func_file.write(func_content)
    func_file.close() 

def name():
    name = input('what is your name? : ')
    print(f'hey {name} , i am cura')
    func_editor('{name}' , f'{name}')

def run():
    reset_file_writer()
    commenter_line_saver()
    name()
    func_commenter("func_editor('{name}' ")
    func_commenter("name = input(")
    func_commenter("data_editor(f'")
    func_commenter("    commenter_line_saver()")
    func_commenter("    reset_file_writer()")
