#Precio de los tratamientos, como son constantes los defino fuera del menu.
Carillas=250000
Implantes=475000
Ortodoncia=800000
t_carilla=0
t_implante=0
t_ortodon=0
subtotal=0
descuento=0
def cotizacion():
    #Muestro las opciones del menu con print
    print("!"*20) 
    print("MENU COTIZACION")
    print("!"*20)
    print("1.- Agregar Tratamientos.\n2.- Calcular total de la cotizacion.\n3.- Imprimir cotizacion.\n4.- Volver al inicio.")
    while True: #Ingreso una validacion para segurarme de que el ingreso de la variable opc, este correcta.
        try:
            opc=int(input("Ingrese su opcion=>>: "))
            if opc<1 or opc>4:
                print("Seleccione una opcion valida")
            else:
                break
        except:
            print("Porfavor, Indique su opcion con el numero correspondiente.")
    if opc==1:  #Pregunto que opcion entro al programa.
        print(f"Tratamientos disponibles \tValor \nCarillas de Porcelana\t        ${Carillas} \nImplantes Dentales\t        ${Implantes} \nCarillas de Porcelana\t        ${Ortodoncia}")
    
    elif opc==2:
        print("Cotizacion:\n")
    elif opc==3:
        print("-"*20)
        print("\tCotizacion:")
        print("-"*20)
        print(f"Subtotal\t${subtotal}\nDescuento %\t${descuento}")
        print("-"*20)

    else:
        print("Volviendo al menu principal...")
    




cotizacion()