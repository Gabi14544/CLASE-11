from banco.gestion import crear_cuenta
from banco.cuentas import CuentaBancaria

def main ():
    cuenta = crear_cuenta()
    print(cuenta.titular, cuenta.saldo)

main()