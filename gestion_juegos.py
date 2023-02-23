import csv
import pandas as pd
import numpy as np
from typing import Any, Hashable, Iterable, Optional



def convert_csv():
    lista = []
    with open('archivo.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            lista.append(row)
    return (lista)


lista = convert_csv()


def buscar_dicc(it: Iterable[dict], clave: Hashable, valor: Any) -> Optional[dict]:
    for dicc in it:
        if dicc[clave] == valor:
            return dicc
    return None


def buscar_varios_dicc(it: Iterable[dict], clave: Hashable, valor: Any) -> Optional[dict]:
    lista_juegos = []
    for dicc in it:
        if dicc[clave] == valor:
            lista_juegos.append(dicc)
    return lista_juegos


def alta_juego(name, platform, year, genre, publisher, na_sales, eu_sales, jp_sales, other_sales, global_sales):
    lista.append({"Name": name,
                  "Platform": platform,
                  "Year": year,
                  "Genre": genre,
                  "Publisher": publisher,
                  "NA_Sales": na_sales,
                  "EU_Sales": eu_sales,
                  "JP_Sales": jp_sales,
                  "Other_Sales": other_sales,
                  "Global_Sales": global_sales})


def alta_juego_input():
    Name = input("Introduce el onmbre del juego que quieres dar de alta:")
    Platform = input("Introduce la plataforma:")
    Year = input("Introduce el año: ")
    Genre = input("Introduce el genero:")
    Publisher = input("Introduce el editor:")
    NA_Sales = input("Introduce las ventas en América ")
    EU_Sales = input("Introduce las ventas en Europa:")
    JP_Sales = input("Introduce las ventas en Japón:")
    Other_Sales = input("Introduce otras ventas:")
    Global_Sales = input("Introduce las ventas globales:")
    alta_juego(Name, Platform, Year, Genre, Publisher, NA_Sales,
               EU_Sales, JP_Sales, Other_Sales, Global_Sales)


def modificar_juego(registro, Name, Platform, Year, Genre, Publisher, NA_Sales,
                    EU_Sales, JP_Sales, Other_Sales, Global_Sales):
    registro.update({"Name": Name, "Platform": Platform, "Year": Year, "Genre": Genre, "Publisher": Publisher, "NA_Sales": NA_Sales,
                    "EU_Sales": EU_Sales, "JP_Sales": JP_Sales, "Other_Sales": Other_Sales, "Global_Sales": Global_Sales})


def modificar_juego_input():
    nombre_juego = input("Dime que juego quieres modificar(nombre exacto): ")
    registro = buscar_dicc(lista, "Name", nombre_juego)

    print("Si presionas enter sin nada, se dejara el valor por defecto")
    print(registro)

    nuevo_nombre_juego = input("Dime el nuevo NOMBRE del juego: ")
    if (nuevo_nombre_juego == ""):
        nuevo_nombre_juego = nombre_juego

    nueva_plataforma_juego = input("Dime la nueva PLATAFORMA del juego: ")
    if (nueva_plataforma_juego == ""):
        nueva_plataforma_juego = registro.get("Platform")

    nuevo_ano_juego = input("Dime el nuevo AÑO de salida del juego: ")
    if (nuevo_ano_juego == ""):
        nuevo_ano_juego = registro.get("Year")

    nuevo_genero_juego = input("Dime el nuevo GENERO del juego: ")
    if (nuevo_genero_juego == ""):
        nuevo_genero_juego = registro.get("Genre")

    nuevo_publisher_juego = input("Dime el nuevo PUBLISHER del juego: ")
    if (nuevo_publisher_juego == ""):
        nuevo_publisher_juego = registro.get("Publisher")

    nuevo_na_sales_juego = input("Dime las nuevas NA SALES del juego: ")
    if (nuevo_na_sales_juego == ""):
        nuevo_na_sales_juego = registro.get("NA_Sales")

    nuevo_eu_sales_juego = input("Dime las nuevas EU SALES del juego: ")
    if (nuevo_eu_sales_juego == ""):
        nuevo_eu_sales_juego = registro.get("EU_Sales")

    nuevo_jp_sales_juego = input("Dime las nuevas JP SALES del juego: ")
    if (nuevo_jp_sales_juego == ""):
        nuevo_jp_sales_juego = registro.get("JP_Sales")

    nuevo_other_sales_juego = input("Dime las nuevas OTHER SALES del juego: ")
    if (nuevo_other_sales_juego == ""):
        nuevo_other_sales_juego = registro.get("Other_Sales")

    nuevo_global_sales_juego = input(
        "Dime las nuevas GLOBAL SALES del juego: ")
    if (nuevo_global_sales_juego == ""):
        nuevo_global_sales_juego = registro.get("Global_Sales")

    modificar_juego(registro, nuevo_nombre_juego, nueva_plataforma_juego,
                    nuevo_ano_juego, nuevo_genero_juego, nuevo_publisher_juego, nuevo_na_sales_juego,
                    nuevo_eu_sales_juego, nuevo_jp_sales_juego, nuevo_other_sales_juego, nuevo_global_sales_juego)


def listar_juego():
    print("| Rank | Name | Platform | Year | Genre | Publisher | NA Sales | EU Sales | JP Sales | Other Sales | Global Sales |")
    limite = 10
    contador = 0
    for elemento in lista:
        contador += 1
        if contador == limite:
            break

        print(" | ", elemento["Rank"], " | ",
              elemento["Name"], " | ",
              elemento["Platform"], " | ",
              elemento["Year"], " | ",
              elemento["Genre"], " | ",
              elemento["Publisher"], " | ",
              elemento["NA_Sales"], " | ",
              elemento["EU_Sales"], " | ",
              elemento["JP_Sales"], " | ",
              elemento["Other_Sales"], " | ",
              elemento["Global_Sales"], " | ")
        print("--------------------------------------------------------------------------------------------------------------------------------------------------------")
        
    

def mas_vendidos_mundo(lista):
    limite = 5
    contador = 0
    i = 0
    while i < len(lista) and contador < limite:
        elemento = lista[i]
        contador += 1
        i += 1
        registro = pd.DataFrame(np.array([[elemento["Rank"], elemento["Name"], elemento["Platform"], elemento["Year"],
        elemento["Genre"], elemento["Publisher"], elemento["NA_Sales"],
        elemento["EU_Sales"], elemento["JP_Sales"], elemento["Other_Sales"],
        elemento["Global_Sales"]]]),
        columns=["Rank", "Name", "Platform", "Year", "Genre", "Publisher",
        "NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales", "Global_Sales"])
        print(registro)
                    
            
            
        




