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
    registro = buscar_dicc(lista, "Name", name)
    mostrar_registro(registro)


def alta_juego_input():
    Name = input("Escribe el nombre del juego que quieres dar de alta:")
    Platform = input("Escribe la plataforma:")
    Year = input("Escribe el año: ")
    Genre = elegir_genero()
    Publisher = input("Escribe el editor:")
    NA_Sales = input("Escribe las ventas en América ")
    EU_Sales = input("Escribe las ventas en Europa:")
    JP_Sales = input("Escribe las ventas en Japón:")
    Other_Sales = input("Escribe otras ventas:")
    Global_Sales = input("Escribe las ventas globales:")
    alta_juego(Name, Platform, Year, Genre, Publisher, NA_Sales,
               EU_Sales, JP_Sales, Other_Sales, Global_Sales)


def borrar_juego():
    Name = input("Selecciona el juego que quieres borrar:")
    lista.remove(buscar_dicc(lista, "Name", Name))
    print("El juego eliminado es ", Name)


def modificar_juego(registro, Name, Platform, Year, Genre, Publisher, NA_Sales,
                    EU_Sales, JP_Sales, Other_Sales, Global_Sales):
    registro.update({"Name": Name, "Platform": Platform, "Year": Year, "Genre": Genre, "Publisher": Publisher, "NA_Sales": NA_Sales,
                    "EU_Sales": EU_Sales, "JP_Sales": JP_Sales, "Other_Sales": Other_Sales, "Global_Sales": Global_Sales})
    mostrar_registro(registro)


def modificar_juego_input():
    nombre_juego = input("Dime que juego quieres modificar(nombre exacto): ")
    registro = buscar_dicc(lista, "Name", nombre_juego)

    print("Si presionas enter sin nada, se dejara el valor por defecto")
    mostrar_registro(registro)

    nuevo_nombre_juego = input("Dime el nuevo NOMBRE del juego: ")
    if (nuevo_nombre_juego == ""):
        nuevo_nombre_juego = nombre_juego

    nueva_plataforma_juego = input("Dime la nueva PLATAFORMA del juego: ")
    if (nueva_plataforma_juego == ""):
        nueva_plataforma_juego = registro.get("Platform")

    nuevo_ano_juego = input("Dime el nuevo AÑO de salida del juego: ")
    if (nuevo_ano_juego == ""):
        nuevo_ano_juego = registro.get("Year")

    nuevo_genero_juego = elegir_genero()
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
    limite = 11
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


def buscar_por_nombre():
    Name = input("Selecciona el juego que quieres buscar:")
    registro = buscar_dicc(lista, "Name", Name)
    mostrar_registro(registro)


def mostrar_registro(elemento):
    print()
    print(" | Name | Platform | Year | Genre | Publisher | NA Sales | EU Sales | JP Sales | Other Sales | Global Sales |")
    print(" | ", elemento["Name"], " | ",
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


def elegir_genero():
    """
    generos = ["Sports", "Platform", "Racing", "Role-playing", "Misc",
               "Shooter", "Simulation", "Action", "Puzzle", "Fighting", "Adventure"]
    """
    generos = []

    for registro in lista:
        generos.append(registro["Genre"])

    generos = list(set(generos))

    print("Elige uno de los siguientes géneros")
    for i in range(len(generos)):
        print(i, "-", generos[i])
    try:
        genero_juego = int(
            input("¿De que género es tu juego, escribe el número? "))
    except:
        print("Pon el número, porfa")

    return generos[genero_juego]


def mas_vendidos_mundo(mas_vendidos):
    limite = 5
    contador = 0
    i = 0
    
    while i < len(mas_vendidos) and contador < limite:
        elemento = mas_vendidos[i]
        contador += 1
        i += 1
        registro = pd.DataFrame(np.array([[elemento["Name"], elemento["Platform"], elemento["Year"],
                                           elemento["Genre"], elemento["Publisher"], elemento["NA_Sales"],
                                           elemento["EU_Sales"], elemento["JP_Sales"], elemento["Other_Sales"],
                                           elemento["Global_Sales"]]]),
                                columns=[ "Name", "Platform", "Year", "Genre", "Publisher",
                                         "NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales", "Global_Sales"])
        print(registro)
        

def obtener_mas_vendidos():
    mas_vendidos = []
    ventas = []
    
    for valor in lista:
        ventas.append(float(valor["Global_Sales"]))
    
    ordenados = sorted(ventas,reverse=True)
    i=0
    
    for i in range(5):
        datos_mas_vendido = buscar_dicc(lista, "Global_Sales", str(ordenados[i]))
        
        mas_vendidos.append(datos_mas_vendido)
        i +=1
    mas_vendidos_mundo(mas_vendidos)
        

def juegos_siglo():
    registros_siglo = []
    for registro in lista:
        year = registro["Year"]
        if year.isdigit() and int(year) >= 1901 and int(year) <= 2000:
            registros_siglo.append(registro)
    lista_juego_2(registros_siglo)


def lista_juegos_genero_input():
    genero = elegir_genero()
    lista_juegos_genero(genero)


def lista_juegos_genero(genero):
    lista_juegos = buscar_varios_dicc(lista, "Genre", genero)
    lista_juego_2(lista_juegos)


def lista_juego_2(lista):
    limite = 11
    contador = 0

    for elemento in lista:
        contador += 1
        if contador == limite:
            break
        registro = pd.DataFrame(np.array([[elemento["Rank"], elemento["Name"], elemento["Platform"], elemento["Year"],
                                           elemento["Genre"], elemento["Publisher"], elemento["NA_Sales"],
                                           elemento["EU_Sales"], elemento["JP_Sales"], elemento["Other_Sales"],
                                           elemento["Global_Sales"]]]),
                                columns=["Rank", "Name", "Platform", "Year", "Genre", "Publisher",
                                         "NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales", "Global_Sales"])
        print(registro)


def elegir_plataforma():

    plataformas = []

    for registro in lista:
        plataformas.append(registro["Platform"])

    plataformas = list(set(plataformas))

    print("Elige una de las siguientes plataformas para buscar todos sus juegos")
    for i in range(len(plataformas)):
        print(i, "-", plataformas[i])
    try:
        genero_juego = int(
            input("¿De que plataforma es tu juego, escribe el número? "))
    except:
        print("Pon el número, porfa")

    return plataformas[genero_juego]


def lista_juegos_plataforma_input():
    plataforma = elegir_plataforma()
    print("Has elegido los juegos para: ", plataforma)
    print("--------------------------------------")
    lista_juegos_plataforma(plataforma)


def lista_juegos_plataforma(plataforma):
    lista_juegos = buscar_varios_dicc(lista, "Platform", plataforma)
    lista_juego_2(lista_juegos)


def elegir_editores():
    editores = ["Nintendo", "Microsoft Game Studios", "Take-Two Interactive", "Sony Computer Entertainment",
                "Activision", "Bethesda Softworks", "Electronic Arts", "Sega", "SquareSoft", "Atari",
                "Ubisoft", "Capcom", "Konami Digital Entertainment", "LucasArts", "505 Games",
                "Virgin Interactive", "Warner Bros"]


def elegir_editores():

    editores = []

    for registro in lista:
        editores.append(registro["Publisher"])

    editores = list(set(editores))

    print("Elige una de las siguientes empresas para buscar todos sus juegos")
    for i in range(len(editores)):
        print(i, "-", editores[i])
    try:
        genero_juego = int(
            input("¿De que empresa es tu juego, escribe el número? "))
    except:
        print("Pon el número, porfa")

    return editores[genero_juego]


def lista_editores_input():
    editor = elegir_editores()
    print("Has elegido a la empresa", editor)
    print("--------------------------------------")
    lista_juegos_editores(editor)


def lista_juegos_editores(editor):
    lista_juegos = buscar_varios_dicc(lista, "Publisher", editor)
    lista_juego_2(lista_juegos)