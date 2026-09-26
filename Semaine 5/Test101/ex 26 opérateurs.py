def operations(a, b):
    if nombre == 1:
        print(a + b)
    elif nombre == 2:
        print(a - b)
    elif nombre == 3:
        print(a * b)
    elif nombre == 4:
        if b == 0:
            print("Impossible")
        else:
            print(a / b)
    else:
        print(a ** b)


while True:
    nombre = int(input("\n1:Addition\n2:Soustraction\n3:multiplication "
                       "\n4:Division\n5:puissance\nchoisissez une opération en inscrivant le nombre accorder:"))
    if 0 < nombre <= 5:
        i = int(input("1er nombre: "))
        y = int(input("2e nombre: "))
        operations(i, y)
    else:
        print("veuillez prendre un nombre disponible")