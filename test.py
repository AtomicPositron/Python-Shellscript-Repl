class Person:
    def __init__(self):
        self.name = ""
        self.age = 0
        self.gender = ""

def add(one,two):
    return one+two
data =  add(1,2)
Person().name = f"{data}"
print(Person().name, data)