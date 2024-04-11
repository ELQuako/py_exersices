def check(string):
    if 'rot' in string:
        return 'Ja'
    else:
        return 'Nein'

A = 'Die Farbe ist rot'
B = check(A)
print(B)

