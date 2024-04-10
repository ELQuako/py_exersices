dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

# Mit der update()-Methode
dict1.update(dict2)
print(dict1)  # Ausgabe: {'a': 1, 'b': 3, 'c': 4}

# Mit dem | Operator 
dict3 = dict1 | dict2
print(dict3)  # Ausgabe: {'a': 1, 'b': 3, 'c': 4}