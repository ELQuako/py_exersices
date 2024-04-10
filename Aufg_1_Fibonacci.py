a = int(input("Geben Sie die Position in der Fibonacci-Reihe ein: "))
b = 0
c = 1

if a <= 0:
    print("Ungültige Eingabe. Die Position muss eine positive ganze Zahl sein.")
else:
    for i in range(1, a):
        b, c = c, b + c
    print("Die Fibonacci-Zahl an Position", a, "ist:", b)
