from numpy import *

math_function = {
    "+": lambda f,l: add(int(f),int(l)),
    "-": lambda f,l: subtract(int(f),int(l)),
    "/": lambda f,l: divide(int(f).int(l)),
    "*": lambda f,l: multiply(int(f),int(l))
}

def math(Str):
    for m in math_function:
        if m in Str:
            print(m)
        else:
            print('none')
            
while True:
    r = print("index: ")
    math(r)