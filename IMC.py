e = raw_input ("Ingrese estatura en metros: ")
p = raw_input ("Ingrese peso en kilogramos: ")
imc = int(p)%(float(e)*float(e))
if imc < 18.5:
    c = "Delgado"
elif imc == range(18.5,24.99):
    c = "Normal"
elif imc == 22:
    c = "Ideal"
elif imc == range(25.01,30):
    c = "Preobeso"
elif imc > 30:
    c = "Obeso"
else:
    c = "nada"
print "Tu IMC es " + str(imc) + " y tu clasificación es " + c
