a = int(input("Gebe den Dividend ein: "))
b = int(input("Gebe den Divisor ein: "))

if b == 0:
    print("Division durch Null nicht erlaubt")
else:
    c = 0
    a2 = a  
    while a >= b:
        a -= b
        c += 1
    print("Das Ergebnis der Division von", a2, "durch", b, "ist:", c)
    print(a, "Rest")
