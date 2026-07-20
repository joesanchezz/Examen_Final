from os import system
system("cls")

def confirmar():
    input("Presione ENTER para continuar...")
    system("cls")

def validarCadena(texto):
    while True:
        cadena=input(f"Ingrese {texto}: ").capitalize()
        if cadena == "" or cadena == " ":
            print(f"{texto} no debe estar vacio")
        else:
            return cadena

def validarEntero(min,texto):
    while True:
        try:    
            num=int(input(f"Ingrese {texto}: "))
            if min<=num:
                return num
            else:
                print(f"{num} debe ser mayor a {min}")
        except:
            print("Debe ingresar un numero entero")



def validarBoolean(texto):
    while True:
        opc=input(f"Tiene {texto}? [s/n]").lower()
        if opc == "s":
            return True
        elif opc=="n":
            return False
        else:
            print("Debe ingresar s (SI) o n (No)")

def validarClasificacion(texto):
    while True:
        cadena=input(f"Ingrese {texto}: ").upper()
        if cadena =="E" or cadena=="T" or cadena =="M" :
            return cadena
        else: print("Debe elegir entre E, T o M")

def leerOpcion():
    while True:
        try:    
            opc=int(input("Eliga una opcion: "))
            if 1<=opc<=6:
                return opc
            else:
                print("Debe seleccionar una opcion valida")
        except:
            print("Debe ingresar un numero entero")

def stockPlataforma(dic_juegos,dic_inventario):
    system("cls")
    plataforma=validarCadena("la plataforma")
    stock=0
    for key in dic_juegos:
            if plataforma in dic_juegos[key]:
               stock+=dic_inventario[key][1]
                
    print(f"El stock disponible es: {stock}")
    confirmar()

def busquedaPrecio(p_min,p_max,dict_inventario):

    for key in dict_inventario:
        precio=dict_inventario[key]
        if p_min< precio <p_max:
            print(dict_inventario[key])