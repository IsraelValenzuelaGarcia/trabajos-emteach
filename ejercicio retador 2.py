Municipios = []
Habitantes = []

Nombre_Municipio = input("Ingresa un municipio: ")
Municipios.append(Nombre_Municipio)
print("El municipio añadido es: "+Nombre_Municipio)
print(Municipios)
Numero_Habitantes1 = int(input("Ingresa el numero de habitantes: "))
Habitantes.append(Numero_Habitantes1)


Nombre_Municipio = input("Ingresa un municipio: ")
Municipios.append(Nombre_Municipio)
print("El municipio añadido es: "+Nombre_Municipio)
print(Municipios)
Numero_Habitantes2 = int(input("Ingresa el numero de habitantes: "))
Habitantes.append(Numero_Habitantes2)

Nombre_Municipio = input("Ingresa un municipio: ")
Municipios.append(Nombre_Municipio)
print("El municipio añadido es: "+Nombre_Municipio)
print(Municipios)
Numero_Habitantes3 = int(input("Ingresa el numero de habitantes: "))
Habitantes.append(Numero_Habitantes3)

total_habitantes = Numero_Habitantes1 + Numero_Habitantes2 + Numero_Habitantes3

habitantes_totales = str(total_habitantes)

print("El total de habitantes es de: " + habitantes_totales)

Promedio_habitantes = total_habitantes/3
habitantes_promedio = str(Promedio_habitantes)
print("El promedio de habitantes es: "+habitantes_promedio)
