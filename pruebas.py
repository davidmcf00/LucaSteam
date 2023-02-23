import unittest
from unittest.mock import patch
from gestion_juegos import *


class Test_lista_juego_genero(unittest.TestCase):

    @patch('builtins.input')
    def test_convert_csv(self):
        with open('archivo.csv', 'r') as file:
            lineas = 0
            for linea in file:
                lineas += 1
        lista = convert_csv()
        self.assertEqual(len(lista), lineas-1)

    def test_lista_juegos_genero(self, mock_input):
        GENERO_A_PROBAR = "Sports"
        lista_por_genero = buscar_varios_dicc(lista, "Genre", GENERO_A_PROBAR)
        self.assertEqual(lista_por_genero[0]["Genre"], GENERO_A_PROBAR)


if __name__ == "__main__":
    unittest.main()
