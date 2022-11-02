import unittest
import cambia_texto


class TestCambiaTexto(unittest.TestCase):

    def test_mayusculas(self):
        palabra = 'Buen día'
        resultado = cambia_texto.todo_mayusculas(palabra)
        self.assertEqual(resultado, 'BUEN DÍA')


if __name__ == '__main__':
    unittest.main()



