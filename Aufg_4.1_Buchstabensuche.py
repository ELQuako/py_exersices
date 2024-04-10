a = input("Bitte geben Sie eine Zeichenkette ein: ")
b = -1

for i in range(len(a)):
    if a[i] == 'a' or a[i] == 'A':
        b = i
        break

if b != -1:
    print("Das erste 'a' oder 'A' befindet sich an der Position:", b)
else:
    print("Es wurde kein 'a' oder 'A' in der Zeichenkette gefunden.")
