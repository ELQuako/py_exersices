def positiv_negative(A):
    if A > 0:
        print("positiv")
    elif A < 0:
        print("negativ")
    else:
        print("null")

A = input("Gib eine Zahl an: ")
positiv_negative(A)