salario = float (input("Ingrese su salario mensual: "))

pago_salud = (salario * 0.4) * 0.125
pago_pension = (salario * 0.4) * 0.16
pago_riesgos =  (salario * 0.4) * 0.00522

print("Pago al sistema de salud = ", pago_salud)
print("Pago al sistema de pension = ", pago_pension)
print("Pago al sistema de riesgos = ", pago_riesgos)

print("Salario neto = ", salario - pago_salud - pago_pension - pago_riesgos)
