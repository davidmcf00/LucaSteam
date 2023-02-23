import os
from gestion_juegos import *


def menu_opciones():

    permanecer = True

    while permanecer:
        mostrar_opciones()
        eleccion = ""
        try:
            eleccion = int(
                input("Seleciona la característica a la que quieres acceder: "))
        except:
            print("Solo acepto las opciones que te di")

        match eleccion:
            case 1:
                os.system('clear')
                alta_juego_input()
            case 2:
                os.system('clear')
                borrar_juego()
            case 3:
                os.system('clear')
                modificar_juego_input()
            case 4:
                os.system('clear')
                listar_juego()
            case 5:
                os.system('clear')
                buscar_por_nombre()
            case 6:
                os.system('clear')
                mas_vendidos_mundo()
            case 7:
                os.system('clear')
                lista_editores_input()
            case 8:
                os.system('clear')
                lista_juegos_plataforma_input()
            case 9:
                os.system('clear')
                juegos_siglo()
            case 10:
                os.system('clear')
                lista_juegos_genero_input()
            case 13:
                os.system('clear')
                print("Adios")
                permanecer = False
            case _:
                os.system('clear')
                print("No se que has seleccionado")


""""
        except:
            os.system('clear')
            print("No se que has seleccionado, solo acepto las siguientes opciones:")
    """


def mostrar_opciones():
    print()
    print("Menu")
    print(" 1 - Insertar un videojuego")
    print(" 2 - Borrar un videojuego")
    print(" 3 - Modificar un videojuego")
    print(" 4 - Listar los videojuegos")
    print(" 5 - Buscar por nombre")
    print(" 6 - Lista de los juegos más vendidos en el mundo")
    print(" 7 - Buscar por listado de los editores")
    print(" 8 - Buscar por plataforma")
    print(" 9 - Listado de juegos del siglo XX")
    print(" 10 - Buscar por género")
    print(" 13 - Salir del programa")
    print("--------------------------------")


menu_opciones()
