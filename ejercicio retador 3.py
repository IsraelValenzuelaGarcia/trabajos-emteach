Peso_admitido_Kg = 1628
Numero_Costales_Cemento_Kg = int(input("Ingrese el numero de costales de cemento: ")) 
Kilos_Cemento = Numero_Costales_Cemento_Kg*40
Kilos_costal_cemento = str(Kilos_Cemento)
print("El peso de los costales de cemento en Kg es: "+Kilos_costal_cemento)

Numero_Costales_Yeso_Kg = int(input("Ingrese el numero de costales de Yeso: ")) 
Kilos_Yeso = Numero_Costales_Yeso_Kg*30
Kilos_costal_yeso = str(Kilos_Yeso)
print("El peso de los costales de yeso en Kg es: "+Kilos_costal_yeso)

peso_total = (Kilos_Cemento + Kilos_Yeso)
peso_total_costales = str(peso_total)
print("El peso total en Kg es: " +peso_total_costales)

Peso_aceptado = peso_total >= 1628 and peso_total <= 3254
print("¿Se puede realizar el envío? ",Peso_aceptado )