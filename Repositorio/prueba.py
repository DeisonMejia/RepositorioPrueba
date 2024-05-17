def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: No se puede dividir por cero"

# Función para la selección de operación
def calcular(operacion, a, b):
    if operacion == '+':
        return suma(a, b)
    elif operacion == '-':
        return resta(a, b)
    elif operacion == '*':
        return multiplicacion(a, b)
    elif operacion == '/':
        return division(a, b)
    else:
        return "Operación no válida"

# Ejemplo de uso
print("Operaciones disponibles: +, -, *, /")
operacion = input("Ingrese la operación que desea realizar: ")
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

resultado = calcular(operacion, num1, num2)
print("El resultado es:", resultado)
