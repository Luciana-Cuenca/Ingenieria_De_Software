alto = float(input('ingrese el alto de la alberca '))
ancho = float(input('ingrese el ancho de la alberca '))
largo = float(input('ingrese el largo de la alberca '))
cubicos = ancho * alto * largo
costo = float(input('ingrese el costo actual del agua por metro cubico'))
total = cubicos * costo
print('El total a pagar es de  ', total )