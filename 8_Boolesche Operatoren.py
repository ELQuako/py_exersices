a = True
b = False

# Boolesches AND
c = a and b
print(c)  # Ausgabe: False

# Boolesches OR
d = a or b
print(d)  # Ausgabe: True

# Boolesches XOR (exklusives OR)
e = a != b
print(e)  # Ausgabe: True

# Identität (prüft, ob zwei Variablen auf dasselbe Objekt verweisen)
f = a is b
print(f)  # Ausgabe: False

g = a is not b
print(g)  # Ausgabe: True

# Zugehörigkeit (prüft, ob ein Wert in einer Sequenz vorhanden ist)
liste1 = [1, 2, 3, 4, 5]
h = 3 in liste1
print(h)  # Ausgabe: True

i = 6 not in liste1
print(i)  # Ausgabe: True