import csv
import os
from typing import Any, Hashable, Iterable, Optional


def convert_csv():
    lista = []
    with open('vgsales.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            lista.append(row)
    return(lista)

def alta_juego_input():
    Name=input("Introduce el juego que quieres dar de alta:")
    Platform=input("Introduce la plataforma:")
    Year=input("Introduce el año: ")
    Genre=input("Introduce el genero:")
    Publisher=input("Introduce el editor:")
    NA_Sales=input("Introduce las ventas en América ")
    EU_Sales=input("Introduce las ventas en Europa:")
    JP_Sales=input("Introduce las ventas en Japón:")
    Other_Sales=input("Introduce otras ventas:")
    Global_Sales=input("Introduce las ventas globales:")
    alta_juego(Name, Platform,Year,Genre,Publisher,NA_Sales,EU_Sales,JP_Sales,Other_Sales,Global_Sales)
        
    
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