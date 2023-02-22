from main import *

lista = pasar_lista()

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

valor = lista.index(buscar_dicc(lista, "Name", "PGA European Tour"))

indice_valor = lista.index(buscar_dicc(lista, "Name", "PGA European Tour"))

juegos_ano_2011 = buscar_varios_dicc(lista, "Year", "2011")

print(valor)
print()
print(indice_valor)
print()
print(juegos_ano_2011)

