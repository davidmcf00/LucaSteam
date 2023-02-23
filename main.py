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
                clear()
                alta_juego_input()
            case 2:
                clear()
                borrar_juego()
            case 3:
                clear()
                modificar_juego_input()
            case 4:
                clear()
                listar_juego()
            case 5:
                clear()
                buscar_por_nombre()
            case 6:
                clear()
                obtener_mas_vendidos()
            case 7:
                clear()
                lista_editores_input()
            case 8:
                clear()
                lista_juegos_plataforma_input()
            case 9:
                clear()
                juegos_siglo()
            case 10:
                clear()
                lista_juegos_genero_input()
            case 13:
                clear()
                print("Adios")
                permanecer = False
            case _:
                clear()
                print("No se que has seleccionado")
                    
"""
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
