baseTerreno =  float(input('introduce la base del terreno'))
alturaTotal =  float(input('introduce la altura total de la figura'))
alturaRectangulo =  float(input('introduce la altura del rectangulo'))
alturaTriangulo = alturaTotal - alturaRectangulo
areaRectangulo = baseTerreno * alturaRectangulo
areaTriangulo = baseTerreno * alturaTriangulo / 2
areaTotal = areaTriangulo + areaRectangulo
print('el area total del terreno es',areaTotal)