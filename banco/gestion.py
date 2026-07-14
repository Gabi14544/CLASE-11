from banco.cuentas import CuentaBancaria

def crear_cuenta():
    user = input("Ingrese su Nombre: ")
    saldo = ""
    while not saldo.isdigit():
        saldo = input("Saldo Inicial: ")
        Saldo_Inicial = int(saldo)
        return CuentaBancaria(user,Saldo_Inicial)


