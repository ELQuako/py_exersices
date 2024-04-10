a = int(input("Geben Sie die erste Zahl ein: "))
b = int(input("Geben Sie die zweite Zahl ein: "))
c = 0

for i in range(b):
    c += a

print("Das Produkt von", a, "und", b, "ist:", c)