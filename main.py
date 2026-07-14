from banco.gestion import crear_cuenta



cuenta = crear_cuenta()
print(cuenta.titular, cuenta.saldo)

while True:
    print(f"\nCuenta de {cuenta.titular} | Saldo: ${cuenta.saldo}")
    print("1.Depositar Dinero")
    print("2.Retirar Dinero")
    print("3.Salir")
    opcion = input("Seleccione una opcion: ")
    if opcion == "1":
        monto_str = input("Monto a Depositar: ")
        if monto_str.isdigit():
            monto = int(monto_str)
            print(cuenta.depositar(monto))
    if opcion == "2":
        pass
    if opcion == "3":
        break