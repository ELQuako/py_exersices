A = input("Gib eine Zahl an: ")
bestimme_vorzeichen(A)

def bestimme_vorzeichen(A):
    if A > 0:
        print("positiv")
    elif A < 0:
        print("negativ")
    else:
        print("null")

