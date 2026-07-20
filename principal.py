from funciones import *
from os import system
system("cls")

juegos = {
'G001': ['Eclipse Runner', 'Pc', 'Accion', 'T', True,
'NovaStudio'],
'G002': ['Puzzle Atlas', 'Switch', 'Puzzle', 'E', False,
'BrightWorks'],
'G003': ['Sky Legends', 'Ps5', 'Aventura', 'T', True,
'OrionGames'],
'G004': ['Racing Pulse', 'Pc', 'Carreras', 'E', True,
'VelocityLab'],
'G005': ['Mystic Farm', 'Switch', 'Simulacion', 'E', False,
'GreenSeed'],
'G006': ['Shadow Tactics', 'Xbox', 'Estrategia', 'M', False,
'IronGate'],
            }

inventario = {
'G001': [9990, 7],
'G002': [19990, 0],
'G003': [42990, 3],
'G004': [14990, 5],
'G005': [17990, 9],
'G006': [39990, 2],
            }

while True:
    print("="*10+"MENU PRINCIPAL"+"="*10)
    print("1.-Stock por plataforma\n2.-Busqueda de juego por rango de precio\n3.-Actualizar precio de juego\n4.-Agregar uego\n5.-Eliminar juego\n6.-Salir")
    print("="*34)
    opc=leerOpcion()
    match opc:
        case 1: 
            stockPlataforma(juegos,inventario)
        case 2:
            min=input("Ingrese el precio minimo: ")
            max=input("Ingrese el precio maximo: ")
            busquedaPrecio(min,max,inventario)
        case 3:
            ""
        case 4:
            ""
        case 5:
            ""

        case 6:
            "Programa Finalizado"
            break