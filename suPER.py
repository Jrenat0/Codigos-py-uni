
lunes=0.05 # DESCUENTO EN TODOS LOS PRODUCTOS CON TODO MEDIO DE PAGO
martes=0.20 # DESCUENTO EN EL TOTAL DE LA COMPRA CON TARJETA DEL SUPERMERCADO
miercoles=0.12 # DESCUENTO EN CARNES CON TODO MEDIO DE PAGO
jueves=0.15 # DESCUENTO EN FRUTAS Y VERDURAS CON TODO MEDIO DE PAGO
viernes=0.10 # DESCUENTO EN VINOS Y LICORES CON TODO MEDIO DE PAGO
linea="-"*50
opc1=0
while opc1!=7:
    print("Opciones de dia: ")
    print("1.-Lunes")
    print("2.-Martes")
    print("3.-Miercoles")
    print("4.-Jueves")
    print("5.-Viernes")
    print("6.-Sabado o domingo")
    print("7.-Salir.")
    while True: #Validacion Del dia
        try:
            opc1=int(input("Ingrese el dia actual: "))
            if opc1>0 and opc1<7:
                dia=opc1
                break
            elif opc1==7:
                break
            else:
                print("Opcion fuera de rango!!")
        except:
            print("Ingrese un NUMERO!!")

    
    while True:  #Validacion Medio de pago
        try:
            print("Ingrese su medio de pago: ")
            print("1.-Tarjeta del supermercado")
            print("2.- Otro medio de pago")
            mediopago=int(input("Ingrese su opcion: "))
            if mediopago>0 and mediopago<3:
                break
            else:
                print("Ingrese una opcion dentro del rango")
        except:
            print("Ingrese un NUMERO!!")

    while True:      # Validacion Total Carne           
        try:
            t_carne=int(input("Ingrese el total de la carne: "))
            if t_carne >=0:
                break
            else:
                raise ValueError()
        except ValueError:
            print("Ingrese un valor mayor o igual a $0")
    
    while True:      # Validacion Total frutas y verduras           
        try:
            t_fyv=int(input("Ingrese el total de las frutas y las verduras: "))
            if t_fyv >=0:
                break
            else:
                raise ValueError()
        except ValueError:
            print("Ingrese un valor mayor o igual a $0")
    
    while True:     #Validacion Total Vinos y licores            
        try:
            t_vinoyl=int(input("Ingrese el total de los vinos y licores: "))
            if t_vinoyl >=0:
                break
            else:
                raise ValueError()
        except ValueError:
            print("Ingrese un valor mayor o igual a $0")

    while True:                 
        try:
            t_otros=int(input("Ingrese el total de otros: "))
            if t_otros >=0:
                break
            else:
                raise ValueError()
        except ValueError:
            print("Ingrese un valor mayor o igual a $0")

    subtotal=t_carne+t_fyv+t_vinoyl+t_otros

    if dia==1:
        descuento=subtotal*lunes
    elif dia==2:
        descuento=subtotal*martes
    elif dia==3:
        descuento=subtotal*miercoles
    elif dia==4:
        descuento=subtotal*jueves
    elif dia==5:
        descuento=subtotal*viernes
    else:
        descuento=0

    print(f"{linea}\n\tSupermercado\n{linea}\nTotal:${subtotal}\nDescuento:${descuento}\n{linea}\nTotal a pagar:${subtotal-descuento}\nGRACIAS POR SU COMPRA")
    
