import os
from gestion_juegos import *

    
def menu_opciones ():
   
    permanecer = True
    
    while permanecer:
        mostrar_opciones()
        try:
            eleccion = int(input("Seleciona la característica a la que quieres acceder: "))
        except:
            print("Solo acepto las opciones que te di")
             
        try:
            match eleccion:
                case 1:
                    os.system('clear')
                    print("Has selecionado el 1")
                case 13:
                    os.system('clear')
                    print("Adios")
                    permanecer = False
                case _:
                    os.system('clear')
                    print("No se que has seleccionado")
        except:
            os.system('clear')
            print("No se que has seleccionado, solo acepto las siguientes opciones:")
            
            
def mostrar_opciones():
    print("Menu")
    print(" 1 - Insertar un videojuego")
    print(" 13 - Salir del programa")
    print("--------------------------------")
        
        
print(convert_csv())
print(alta_juego_input())
