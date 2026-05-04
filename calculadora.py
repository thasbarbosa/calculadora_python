# Calculadora

a = float(input("Introduzca el valor que quieras calcular: "))
b = float(input("Introduzca el segundo valor que quieras calcular: "))
op = input("Introduce la operación que quieras calcular: ")
if op == '+' :print(a+b)
elif op == '-' :print(a-b)
elif op == '*' :print(a*b)
elif op == '/' :print(a/b)
else: print("Valor no valido")
