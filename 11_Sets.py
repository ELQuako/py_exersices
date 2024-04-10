set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Vereinigung
a = set1 | set2  
print(a)  # Ausgabe: {1, 2, 3, 4, 5}

# Schnittmenge
b = set1 & set2  
print(b)  # Ausgabe: {3}

# Differenz
c = set1 - set2  
print(c)  # Ausgabe: {1, 2}

# Symmetrische Differenz
d = set1 ^ set2  
print(d)  # Ausgabe: {1, 2, 4, 5}