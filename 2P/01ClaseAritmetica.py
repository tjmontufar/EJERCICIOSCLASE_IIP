class OperacionesAritmeticas:
    import os
    os.system('cls' if os.name == 'nt' else 'clear')
    def __init__(self, a=int(input("Valor A: ")), b=int(input("Valor B: "))):
        self.a = a
        self.b = b
    
    # Suma
    def suma(self):
        print("Suma: ",self.a + self.b)
    
    # Resta
    def resta(self):
        print("Resta: ",self.a - self.b)

    # Multiplicacion
    def multiplicacion(self):
        print("Multiplicacion: ",self.a * self.b)
    
    # Division
    def division(self):
        if(self.b == 0):
            print("No se puede dividir entre cero.")
        else:
            print("Division: ",self.a / self.b)
    
    # Potencia
    def potencia(self):
        print("Potencia: ",self.a ** self.b)

ejecutar = OperacionesAritmeticas()
ejecutar.suma()
ejecutar.resta()
ejecutar.multiplicacion()
ejecutar.division()
ejecutar.potencia()