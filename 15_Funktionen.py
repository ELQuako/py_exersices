def funktion(name, alter):
    print("Name:", name)
    print("Alter:", alter)

def func1(*args):
    for i in args:
        print(i)
        
def calculation(a, b):
    return a + b, a - b     

def show_employee(name, gehalt=9000):
    print("Name:", name, "gehalt:", gehalt)   
    
def outer_funct(a, b):
    quadrat = a ** 2

    def addition(a, b):
        return a + b
    add = addition(a, b)
    return add + 5    

name = "Leon"
alter = 18
funktion(name, alter)
func1(20, 40, 60)
func1(80, 100)
add, sub = calculation(40, 10)
print(add, sub)
show_employee("Ignaz", 12000)
show_employee("Leon")
ergebnis = outer_funct(5, 10)
print(ergebnis)


