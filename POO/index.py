from POOPython import coche, CuentaBancaria, Rectangulo
c=coche()
cuenta=CuentaBancaria()
rect=Rectangulo()
while True:
    print("1. Coche")
    print("2. Cuenta Bancaria")
    print("3. Rectangulo")
    print("4. Salir")
    opcion=int(input("Selecciona una opcion: "))
    match opcion:
        case 1:
            print("1. Acelerar")
            print("2. Frenar")
            print("3. Mostrar informacion")
            sub=int(input("Opcion: "))
            match sub:
                case 1:
                    vel = int(input("Velocidad a aumentar: "))
                    c.acelerar(vel)
                case 2:
                    vel = int(input("Velocidad a frenar: "))
                    c.frenar(vel)
                case 3:
                    c.mostrar_info()
                case _:
                    print("Opcion invalida en coche")
            #Cuenta bancaria
        case 2:
            print("1. Depositar")
            print("2. Retirar")
            print("3. Mostrar saldo")
            sub=int(input("Opcion: "))
            match sub:
                case 1:
                    cant = float(input("Cantidad a depositar: "))
                    cuenta.depositar(cant)
                case 2:
                    cant = float(input("Cantidad a retirar: "))
                    cuenta.retirar(cant)
                case 3:
                    cuenta.mostrar_saldo()
                case _:
                    print("Opcion invalida en cuenta")
        case 3:
            print("Calcular area y perimetro")
            rect.base = float(input("Ingresa la base: "))
            rect.altura = float(input("Ingresa la altura: "))
            rect.mostrar_info()
        case 4:
            print("Cerrando el programa")
            break
        case _:
            print("Opcion invalida en menu principal")