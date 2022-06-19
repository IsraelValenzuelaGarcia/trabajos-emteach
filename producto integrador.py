Numero_Cajas_En_Venta = int(input("Ingrese el numero de cajas: "))

producto_id = int(input("Ingresa la id del producto: "))

Caja_maizgrano = Numero_Cajas_En_Venta * 285.55 + 1500
Caja_de_maizgrano = Numero_Cajas_En_Venta * 285.55
descuento_maizgrano = Caja_de_maizgrano * 0.20
Caja_maizgrano_descuento = Caja_de_maizgrano - descuento_maizgrano 

Caja_pepino = Numero_Cajas_En_Venta * 334.72 + 1500
Caja_de_pepino = Numero_Cajas_En_Venta * 334.72
descuento_pepino = Caja_de_pepino * 0.20
Caja_pepino_descuento = Caja_de_pepino - descuento_pepino 

Caja_tomate_verde = Numero_Cajas_En_Venta * 129.00 + 1500
Caja_de_tomate_verde = Numero_Cajas_En_Venta * 129.00
descuento_tomate_verde = Caja_de_tomate_verde * 0.20
Caja_tomate_verde_descuento = Caja_de_tomate_verde - descuento_tomate_verde 

if producto_id == 1 and Numero_Cajas_En_Venta <=100:
  print("El producto es: Maíz grano")
  print("El precio de caja es de: 285.55")
  print("¿Se puede aplicar el descuento? False ")
  print("El costo total a pagar es de: ",Caja_maizgrano )

elif producto_id == 1 and Numero_Cajas_En_Venta <1500: 
  print("El producto es: Maíz grano")
  print("El precio de caja es de: 285.55")
  print("¿Se puede aplicar el descuento? True ")
  print("El costo total a pagar es de: ",Caja_maizgrano_descuento)

elif producto_id == 2 and Numero_Cajas_En_Venta <=100: 
  print("El producto es: pepino")
  print("El precio de caja es de: 334.72")
  print("¿Se puede aplicar el descuento? False ")
  print("El costo total a pagar es de: ",Caja_pepino)

elif producto_id == 2 and Numero_Cajas_En_Venta <1500: 
  print("El producto es: pepino")
  print("El precio de caja es de: 334.72")
  print("¿Se puede aplicar el descuento? True ")
  print("El costo total a pagar es de: ",Caja_pepino_descuento)

  
elif producto_id == 3 and Numero_Cajas_En_Venta <=100: 
  print("El producto es: tomate_verde")
  print("El precio de caja es de: 129.00")
  print("¿Se puede aplicar el descuento? False ")
  print("El costo total a pagar es de: ",Caja_tomate_verde)

elif producto_id == 3 and Numero_Cajas_En_Venta <1500: 
  print("El producto es: tomate_verde")
  print("El precio de caja es de: 129.00")
  print("¿Se puede aplicar el descuento? True ")
  print("El costo total a pagar es de: ",Caja_tomate_verde_descuento)
  
  
else:
  print("Id invalida, por favor seleccione una del 1 al 3")