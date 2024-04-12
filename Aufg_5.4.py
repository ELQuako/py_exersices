def check(A):
    if 'rot' in A:
        return 'Ja'
    else:
        return 'Nein'

A = 'Die Farbe ist rot'
B = check(A)
print(B)
