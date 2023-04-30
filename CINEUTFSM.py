boletos=0      #Cantidad de boletos a llevar y los precios de las entradas.
estreno=4800
normal=2900

palomitas=0
p_pequeñas=2500
p_medianas=4500
p_grandes=7800

bebidas=0
b_pequeñas=1000
b_medianas=1250
b_grandes=2000


opc=0 #Variable dedicada a las opciones del menu.


usm=False #Variable dedicada a indicar si el cliente pertenece al establecimiento o no.
opc=int(input("¿El cliente es estudiante o funcionario de la universidad?:\n1.-SI\n2.-NO"))
while opc<1 or opc>2: #Valido que la opcion este entre alguna de las posibles.
    print("Porfavor, seleccione una opcion valida ingresando el numero correspondiente!!")
    opc=int(input("¿El cliente es estudiante o funcionario de la universidad?:\n1.-SI\n2.-NO"))
if opc==1: 
    usm=True
    opc=0   #Reincio mi variable opc para dsps ocuparla sin problemas.
else:
    opc=0


print(f"{opc},{usm}")


opc=int(input(f"¿Que tipo de entrada desea ver?:\n1.-Estreno (Valor:${estreno})\n2.-Normal(Valor:${normal})"))
while opc<1 or opc>2: #Valido que la opcion este entre alguna de las posibles.
    print("Porfavor, seleccione una opcion valida ingresando el numero correspondiente!!")
    opc=int(input(f"¿Que tipo de entrada desea ver?:\n1.-Estreno (Valor:${estreno})\n2.-Normal(Valor:${normal})"))


boletos=int(input("¿Cuantos boletos van a llevar?:"))
while boletos<1:
    print("Seleccione una cantidad mayor que 0!!")
    boletos=int(input("¿Cuantos boletos van a llevar?:"))


if opc==1:
    boletos=boletos*estreno
else:
    boletos=boletos*normal


print(f"{boletos}")


opc=int(input("¿Desea agregar palomitas de maíz a su pedido?:\n1.-SI\n2.-NO"))
while opc<1 or opc>2:
    print("Porfavor, seleccione una opcion valida ingresando el numero correspondiente!!")
    opc=int(input("¿Desea agregar palomitas de maíz a su pedido?:\n1.-SI\n2.-NO"))


if opc==1:
    opc=int(input(f"¿De que tamaño las palomitas?:\n1.-Pequeñas (Valor:${p_pequeñas})\n2.-Medianas(Valor:${p_medianas})\n3.-Grandes(Valor:${p_grandes})"))
    while opc<1 or opc>3: #Valido que la opcion este entre alguna de las posibles.
        print("Porfavor, seleccione una opcion valida ingresando el numero correspondiente!!")
        opc=int(input(f"¿De que tamaño las palomitas?:\n1.-Pequeñas (Valor:${p_pequeñas})\n2.-Medianas(Valor:${p_medianas})\n3.-Grandes(Valor:${p_grandes})")) 


    palomitas=int(input("¿Cuantas va a llevar?:"))
    while palomitas<1:
        print("Seleccione una cantidad mayor que 0!!")
        palomitas=int(input("¿Cuantas va a llevar?:"))

    if opc==1:
        palomitas=palomitas*p_pequeñas
    elif opc==2:
        palomitas=palomitas*p_medianas
    else:
        palomitas=palomitas*p_grandes
    

    print(f"{palomitas}")


opc=int(input("¿Desea agregar bebidas a su pedido?:\n1.-SI\n2.-NO"))
while opc<1 or opc>2:
    print("Porfavor, seleccione una opcion valida ingresando el numero correspondiente!!")
    opc=int(input("¿Desea agregar bebidas a su pedido?:\n1.-SI\n2.-NO"))


if opc==1:
    opc=int(input(f"¿De que tamaño las bebidas?:\n1.-Pequeñas (Valor:${b_pequeñas})\n2.-Medianas(Valor:${b_medianas})\n3.-Grandes(Valor:${b_grandes})"))
    while opc<1 or opc>3: #Valido que la opcion este entre alguna de las posibles.
        print("Porfavor, seleccione una opcion valida ingresando el numero correspondiente!!")
        opc=int(input(f"¿De que tamaño las bebidas?:\n1.-Pequeñas (Valor:${b_pequeñas})\n2.-Medianas(Valor:${b_medianas})\n3.-Grandes(Valor:${b_grandes})")) 
    
    bebidas=int(input("¿Cuantas va a llevar?:"))
    while bebidas<1:
        print("Seleccione una cantidad mayor que 0!!")
        bebidas=int(input("¿Cuantas va a llevar?:"))


    if opc==1:
         bebidas=bebidas*b_pequeñas
    elif opc==2:
         bebidas=bebidas*b_medianas
    else:
         bebidas=bebidas*b_grandes  

    
    print(f"{bebidas}")

if usm:
    total=(boletos*0.30)+palomitas+bebidas
else:
    total=boletos+palomitas+bebidas

print(f"El total a pagar es de ${total}")

vuelto=int(input("Ingrese la cantidad de efectivo entregado:"))
vuelto=vuelto-total

print(f"El vuelto es de ${vuelto}")