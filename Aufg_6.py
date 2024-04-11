# (a) Funktion zur Berechnung der Summe von a, b, c, und d
def sum(a, b, c, d):
    return a + b + c + d

# (b) Funktion zur Umkehrung eines Arrays
def revert(array):
    return array[::-1]

# (c) Funktion zur Beschränkung eines Arrays von Index x bis y
def trim(array, x, y):
    return array[x:y+1]

# (d) Funktion zum Vergleich von zwei Werten auf Wert und Typ
def compare(a, b):
    if a == b:
        return "Wert ist gleich."
    elif type(a) == type(b):
        return "Typ ist gleich."
    else:
        return "Werte sind ungleich."

# Beispielaufrufe:
print(sum(1, 2, 3, 4))            # Ausgabe: 10
print(revert([2, 4, 6]))           # Ausgabe: [6, 4, 2]
print(trim([0, 1, 2, 3, 4], 1, 3)) # Ausgabe: [1, 2, 3]
print(compare(5, 5.0))             # Ausgabe: Wert ist gleich.
print(compare(3.141, 2.718))       # Ausgabe: Typ ist gleich.