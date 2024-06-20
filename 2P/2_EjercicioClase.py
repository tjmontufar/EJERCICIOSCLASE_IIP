# Crea una función llamada devolver_distintos() que reciba 3
# integers como parámetros.
# Si la suma de los 3 numeros es mayor a 15, va a devolver el
# número mayor.
# Si la suma de los 3 numeros es menor a 10, va a devolver el
# número menor.
# Si la suma de los 3 números es un valor entre 10 y 15
# (incluidos) va a devolver el número de valor intermedio.

def devolver_distintos(n1,n2,n3):
    sumatoria = n1 + n2 + n3
    if(sumatoria > 15):
        resultado = max(n1,n2,n3)
    elif(sumatoria < 10):
        resultado = min(n1,n2,n3)
    else:
        resultado = n1+n2+n3-max(n1,n2,n3)-min(n1,n2,n3)
    return resultado

a = int(input("Ingrese el valor A: "))
b = int(input("Ingrese el valor B: "))
c = int(input("Ingrese el valor C: "))

print(devolver_distintos(a,b,c))