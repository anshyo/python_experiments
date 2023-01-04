import _func

if __name__ == '__main__' :
    a = input('What do you wanna do?( reset("r") / run normally("n") ) / to change your name("c") : ').lower()
    if a == 'r':
        _func.reset()
    elif a == 'n':
        _func.run()