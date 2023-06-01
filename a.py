opc1=0
c_carillas=0
c_implantes=0
c_ortodoncia=0

tipotrabajador=0
dscto=0

carillas=250000
implantes=475000
ortodoncia=800000

while opc1 !=3: #Menu
    print("1.-Cotizacion")
    print("2.-Reiniciar la cotizacion")
    print("3.-Salir del programa")
    while True: #Validacion de variable
        try:
            opc1=int(input("Ingrese una opcion: "))
            if opc1>0 and opc1<4:
                break
            else:
                print("Porfavor, ingrese una opcion valida.")
        except:
            print("Porfavor ingrese un NUMERO!!")
    if opc1==1:
        opc2=0
        while opc2!=4:
            print("1.-Carillas porcelana $250.000")
            print("2.-Implantes dentales $475.000")
            print("3.-Ortodoncia Brackets $800.000")
            print("4.-Salir")


            while True: #Validacion de variable
                try:
                    opc2=int(input("Ingrese una opcion: "))
                    if opc2>0 and opc2<5:
                        break
                    else:
                        print("Porfavor, ingrese una opcion valida.")
                except:
                    print("Porfavor ingrese un NUMERO!!")

            
            if opc2==1:
                c_carillas+=1
            elif opc2==2:
                c_implantes+=1
            elif opc2==3:
                c_ortodoncia+=1
            else:
                print("1.- Trabajador Auxiliar 15%")
                print("2.- Trabajador Administrativo 10%")
                print("3.- Trabajador Docente 5%")
                print("4.- Otro")

                
                while True: #Validacion de variable
                    try:
                        tipotrabajador=int(input("Ingrese el tipo de trabajador: "))
                        if tipotrabajador>0 and tipotrabajador<5:
                            break
                        else:
                            print("Porfavor, ingrese una opcion valida.")
                    except:
                        print("Porfavor ingrese un NUMERO!!")
                
                
                if tipotrabajador==1:
                    dscto=15
                elif tipotrabajador==2:
                    dscto=10
                elif tipotrabajador==3:
                    dscto=5
                else:
                    dscto=0
        subtotal=(c_carillas*carillas)+(c_implantes*implantes)+(c_ortodoncia*ortodoncia)
        print("-"*50)        
        print("\tCotizacion:")
        print("-"*50)
        if c_carillas>0:
            print(f"==>{c_carillas} Tratamientos de carilla porcelana: ${c_carillas*carillas}")
        if c_implantes>0:
            print(f"==>{c_implantes} Tratamientos de Implantes Dentales: ${c_implantes*implantes}")
        if c_ortodoncia>0:
            print(f"==>{c_ortodoncia} Tratamientos de carilla porcelana: ${c_ortodoncia*ortodoncia}")
        print("-"*50)
        print(f"Subtotal:\t{subtotal}")
        print(f"Descuento {dscto}%: \t${subtotal*(dscto/100)}")
        print("-"*50)
        print(f"Total:\t{subtotal-(subtotal*(dscto/100))}")
        print("-"*50)
        print(f"Son 12 Cuotas de:\t{round((subtotal-(subtotal*(dscto/100)))/12)}")
    
    elif opc1==2:
        c_carillas=0
        c_implantes=0
        c_ortodoncia=0
        tipotrabajador=0
        dscto=0
        print("Reiniciando cotizacion...")
    else:
        print("Chao pescao.")




        
            

            
        