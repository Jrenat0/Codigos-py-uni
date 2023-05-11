###Una jugueteria tiene mucho exito en dos de sus productos: payasos y muñecas. Generalmente, realiza ventas por correo.#
#La empresa de logistica les cobra por peso de cada paquete, asi que deben calcular el peso de los payasos y muñecas que saldran en cada paquete a demanda. Cada payaso#
#pesa 112 g y cada muñeca 75g. Escribir un programa que lea el numero de payasos y muñecas vendidos en el ultimo pedido y calcule el peso total del paquete que sera enviado.#
#Considere crear un menu para hacer el calculo en reiteradas ocasiones. No olvide validar#

peso_p=112  #Peso de payasos en gramos
peso_m=75   #Peso de muñecos en gramos
def pesopaquete():
    while True:
        try:
            p=int(input("Ingrese la cantidad de payasos que contiene el paquete: "))
            if p<0:
                print("Ingrese una cantidad igual o mayor a 0")
            else:
                break
        except:
            print("Porfavor, indique la cantidad de articulos con numeros positivos enteros.")


    while True:
        try:
            m=int(input("Ingrese la cantidad de muñecos que contiene el paquete: "))
            if m<0:
                print("Ingrese una cantidad igual o mayor a 0")
            elif m+p==0:
                print("Porfavor ingrese almenos 1 articulo dentro del paquete para proceder.")
            else:
                break
        except:
            print("Porfavor, indique la cantidad de articulos con numeros positivos enteros.")

    print(f"El pedido contiene {p+m} articulos con un peso total de {(p*peso_p)+(m*peso_m)}[g]")


while True:
    print("+"*25)
    print("MENU REGISTRO DE ENVIO")
    print("+"*25)
    print("1.-Calcular el peso de un paquete")
    print("2.-Salir del programa")
    while True:
        try:
            opc=int(input("Seleccione una opcion: "))
            if opc<1 or opc>2:
                print("Ingrese alguna de las 2 opciones")
            else:
                break
        except:
            print("Indique su opcion con un numero entero")
    if opc==1:
        pesopaquete()
    else:
        break