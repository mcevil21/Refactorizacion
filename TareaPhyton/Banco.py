class CuentaBancaria:
    def __init__(self, saldo_inicial):
        self.saldo = saldo_inicial
    def actualizar_saldo(self):
        if self.saldo < 10000.00:
            self.saldo *= (1 + 0.03)
        else:
            self.saldo *= (1 + 0.04)
    def mostrar_saldo(self):
        print(f"Saldo final es {self.saldo:5.2f}")
def main():
    try:
        saldo_inicial = float(input('Dame saldo actual: '))
        cuenta = CuentaBancaria(saldo_inicial)
        cuenta.actualizar_saldo()
        cuenta.mostrar_saldo()
    except ValueError:
        print("Por favor, introduce un número válido.")