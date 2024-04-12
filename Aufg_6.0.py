# (a) 
def sum(a, b, c, d):
    return a + b + c + d

# (b) 
def revert(array):
    return array[::-1]

# (c) 
def trim(array, x, y):
    return array[x:y+1]

# (d) 
def compare(a, b):
    if a == b:
        return "Wert ist gleich."
    elif type(a) == type(b):
        return "Typ ist gleich."
    else:
        return "Werte sind ungleich."


print(sum(1, 2, 3, 4))            
print(revert([2, 4, 6]))           
print(trim([0, 1, 2, 3, 4], 1, 3)) 
print(compare(5, 5.0))             
print(compare(3.141, 2.718))       