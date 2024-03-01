#input

salario_emp = int(input("digite el salario del emplado: "))
deudas = input("el empleado tiene deudas si,no: ")

#procissing

if salario_emp>=945200:
    if deudas == "no":
            rta = "APROBADO"
    else:
        rta = "RECHAZADO"
else:
    rta = "RECHAZAO"

#output
    
print("su prestamo ha sido " + rta)