import csv
from typing import Any, Hashable, Iterable, Optional


def convert_csv():
    lista = []
    with open('archivo.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            lista.append(row)
    return(lista)

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
                  "JP_Sales":jp_sales,
                  "Other_Sales": other_sales,
                  "Global_Sales": global_sales})


def alta_juego_input():
    Name=input("Introduce el onmbre del juego que quieres dar de alta:")
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