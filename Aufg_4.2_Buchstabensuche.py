a = input("Bitte geben Sie eine Zeichenkette ein: ")
b = []

for i in range(len(a)):
    if a[i] == 'a' or a[i] == 'A':
        b.append(i)

if b:
    print("Die Positionen von 'a' oder 'A' in der Zeichenkette sind:", b)
else:
    print("Es wurde kein 'a' oder 'A' in der Zeichenkette gefunden.")
