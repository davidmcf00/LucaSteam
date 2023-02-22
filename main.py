import csv
import os
from typing import Any, Hashable, Iterable, Optional


def pasar_lista():
    lista = []
    with open('vgsales.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            lista.append(row)
    return(lista)
        

    
def mostrar_opciones ():
    menu_principal()
    permanecer = True
    
    while permanecer:
        try:
            eleccion = int(input("Dígame una cantidad en pesetas: "))
        except:
            print("Solo acepto las opciones que te di")
             
        try:
            match eleccion:
                case 1:
                    print("Has selecionado el 1")
                case 2:
                    print("Has selecionado el 2")
                case 3:
                    print("Has selecionado el 3")
                case 4:
                    print("Has selecionado el 4")
                case 13:
                    print("Adios")
                    permanecer = False
                case _:
                    print("Estoy muerto")
        except:
            print("No se que has seleccionado")
            
            
def menu_principal():
    print("Menu")
    print(" 1 - Insertar un videojuego")
    print(" 2 - Eliminar un videojuego")
    print(" 3 - Modificar un videojuego")
    print(" 4 - Listar los videojuegos")
    print(" 13 - Salir del programa")
    print("--------------------------------")
        
        
mostrar_opciones()