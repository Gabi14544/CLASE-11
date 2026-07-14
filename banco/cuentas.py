class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.saldo = saldo_inicial
    
    def depositar(self,monto:int):#Hcerlo despues con otra menera
        if monto > 0:
            self.saldo += monto
            return f"Ingreso exitoso.Nuevo saldo ${self.saldo}"
        return "Monto Invalido"

    def retirar(self,monto:int):
        pass
