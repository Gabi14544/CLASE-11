class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.saldo = saldo_inicial
    
    def depositar(self,monto:int):#Hcerlo despues con otra menera
        if monto > 0:
            self.saldo += monto
            return f"Ingreso Exitoso. Nuevo saldo: {self.saldo}"
        return "Ingreso no Valido"

    def retirar(self,monto:int):
        if monto > 0:
            self.saldo -= monto
            return f"Retiro Exitoso. Nuevo saldo: {self.saldo}"
        return "Ingreso No valido"
    
