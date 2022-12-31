data_list = {}
name = ''
def func_editor(changing , change):
    func_content = ''
    func_file = open('mutable A.I\_func.py' , 'r')
    for line in func_file:
        if changing in line:
            func_content += line.replace(changing , change)
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
            comment = '#'+start
            func_content += line.replace(start , comment)
        else:
            func_content += line
    func_file.close()
    func_file = open('mutable A.I\_func.py' , 'w')
    func_file.write(func_content)
    func_file.close() 

def data_editor(change):
    data_file = open('mutable A.I\data.txt' , 'a')
    data_file.write(change + '\n')
    data_file.close() 

def data_fetcher():
    data_file = open('mutable A.I\data.txt' , 'r')
    for line in data_file:
        global data_list
        data_list = line
    data_file.close()

def welcome():
    global name
    name = input('what is your name? : ')
    print(f'hey {name} , i am cura')
    data_editor(f'name:{name};')
    func_editor('{name}' , f'{name}')

def run():
    welcome()
    data_fetcher()
    func_commenter("func_editor('ansh")
    func_commenter("name = input(")
    func_commenter("data_editor(f'")
# print(data_list)