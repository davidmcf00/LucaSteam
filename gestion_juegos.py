from main import *

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





