#programa parasaber de acuerdo a su estatura y su peso su estadde salud imc 

# input 
peso= int(input("por favor ingrese su peso : "))
altura = float(input("por favor ingrese su altura : "))

# processig 
imc = peso/altura**2

if imc < 16:
    resultado ="criterio de ingreso de hospital"
elif imc <= 17:
    resutado = " infrapeso"
elif imc <= 18:
    resultado = "bajo peso"
elif imc <= 25:
    resultado = "peso normal (saludable)"
elif imc <= 30:
    resultado = "sobre peso(obesidad de grado 1)"
elif imc <= 35:
    resultado = "sobre peso cronico(obesidad de grado 2)"
elif imc <= 40:
    resultado = "obesidad pre morbida (obesidad de grado 3 )"
elif imc >= 40:
    resultado = "obesidad morbida (obesidad de grado 4)"

# output

print("su imc es" ,imc,"y sus resultados son ",resultado,)
