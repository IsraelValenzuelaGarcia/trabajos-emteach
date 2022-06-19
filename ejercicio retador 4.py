

Numero_Cajas_En_Venta = int(input("Ingrese el numero de cajas: "))

producto_id = input("Ingresa la id del producto: ")

if producto_id == "1":
  print("El producto es: Maíz grano")
  if producto_id == "1":
    print("El precio de caja es de: 285.55")
    if producto_id == "1":
      Numero_Cajas = Numero_Cajas_En_Venta*285.55
      Cajas_a_vender = str(Numero_Cajas)
      print("El costo total a pagar es de: "+Cajas_a_vender)
      if Numero_Cajas_En_Venta <= 100:
        Costo_envio = Numero_Cajas+1500
        Costo_envio_2 = str(Costo_envio)
        print("El costo total a pagar mas envio es de: "+ Costo_envio_2)
      
      




      
elif producto_id == "2":
  print("El producto es: Pepino")
  if producto_id == "2":
    print("El precio de caja es de: 334.72")
    if producto_id == "2":
      Numero_Cajas = Numero_Cajas_En_Venta*334.72
      Cajas_a_vender = str(Numero_Cajas)
      print("El costo total a pagar es de: "+Cajas_a_vender)
      if Numero_Cajas_En_Venta <= 100:
        Costo_envio = Numero_Cajas+1500
        Costo_envio_2 = str(Costo_envio)
        print("El costo total a pagar mas envio es de: "+ Costo_envio_2)


    
elif producto_id == "3":
  print("El producto es: Tomate Verde")
  if producto_id == "3":
    print("El precio de caja es de: 129.00")
    if producto_id == "3":
      Numero_Cajas = Numero_Cajas_En_Venta*129.00
      Cajas_a_vender = str(Numero_Cajas)
      print("El costo total a pagar es de: "+Cajas_a_vender)
      if Numero_Cajas_En_Venta <= 100:
        Costo_envio = Numero_Cajas+1500
        Costo_envio_2 = str(Costo_envio)
        print("El costo total a pagar mas envio es de: "+ Costo_envio_2)
else:
  print("Id invalida")
  

  
