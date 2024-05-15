from io import StringIO
import unittest

"""Para hacer que las pruebas corra importamos sys"""
import sys
from unittest.mock import patch
sys.path.append("src")


from console.huffman_menu import HuffmanMenu
from logica.huffman_cleanCode import HuffmanCoding
from model.Registros import Registro
import controller.ControladorRegistros as ControladorRegistros


class TestHuffmanCoding(unittest.TestCase):
    
    SPECIAL_CHARACTER_TEST = "!@#$%^&*()"
    WORD_TEST = "abracadabra"
    REPEATED_CHARACTERS_TEST = "aaaaabbbbccccc"
    
    def setUp(self):
        """ Se ejecuta siempre antes de cada metodo de prueba """
        print("Invocando setUp")
        ControladorRegistros.CrearTabla()
        ControladorRegistros.BorrarFilas()
    
    def test_encode_normal_text(self):
        """Prueba normal: Comprime un texto normal y verifica el resultado"""
        coding = HuffmanCoding()
        encoded = coding.encode(self.WORD_TEST)
        expected_result = "110111001100110010110110001101101111110011011100110011001011011"
        self.assertEqual(encoded, expected_result)

    def test_decode_normal_text(self):
        """Prueba normal: Descomprime un texto normal y verifica el resultado"""
        coding = HuffmanCoding()
        encoded = coding.encode(self.WORD_TEST)
        decoded = coding.decode(encoded)
        self.assertEqual(decoded, self.WORD_TEST)

    def test_encode_special_characters(self):
        """Prueba normal: Comprime un texto con caracteres especiales y verifica el resultado"""
        coding = HuffmanCoding()
        encoded = coding.encode(self.SPECIAL_CHARACTER_TEST)
        expected_result = "0101000001111010011010010101100111000101110101010100101110010101001000"
        self.assertEqual(encoded, expected_result)

    def test_decode_special_characters(self):
        """Prueba normal: Descomprime un texto con caracteres especiales y verifica el resultado"""
        coding = HuffmanCoding()
        encoded = coding.encode(self.SPECIAL_CHARACTER_TEST)
        decoded = coding.decode(encoded)
        self.assertEqual(decoded, self.SPECIAL_CHARACTER_TEST)

    def test_encode_repeated_characters(self):
        """Prueba normal: Comprime un texto con caracteres repetidos y verifica el resultado"""
        coding = HuffmanCoding()
        encoded = coding.encode(self.REPEATED_CHARACTERS_TEST)
        expected_result = "11011110111101111011110111001100100110010011001001100000110000110000110000110000110"
        self.assertEqual(encoded, expected_result)

    def test_decode_repeated_characters(self):
        """Prueba normal: Descomprime un texto con caracteres repetidos y verifica el resultado"""
        coding = HuffmanCoding()
        encoded = coding.encode(self.REPEATED_CHARACTERS_TEST)
        decoded = coding.decode(encoded)
        self.assertEqual(decoded, self.REPEATED_CHARACTERS_TEST)

    def test_none_text(self):
        """Prueba excepcional: Intenta comprimir un texto que es None y verifica la excepción"""
        with self.assertRaises(ValueError):
            coding = HuffmanCoding()
            coding.encode(None)

    def test_empty_text(self):
        """Prueba excepcional: Descomprime un texto con texto vacío y verifica la excepción"""
        with self.assertRaises(ValueError):
            coding = HuffmanCoding()
            coding.decode("")
            
    def test_encode_invalid_text_type(self):
        """Prueba excepcional: Intenta comprimir un texto que no es de tipo string y verifica la excepción"""
        coding = HuffmanCoding()
        with self.assertRaises(TypeError):
            coding.encode(123)

    def test_decode_long_text(self):
        """Prueba de error: Descomprime un texto largo y verifica que el resultado sea igual al texto original"""
        text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
        coding = HuffmanCoding()
        encoded = coding.encode(text)
        decoded = coding.decode(encoded)
        self.assertEqual(decoded, text)

    def test_decode_invalid_character_in_encoded_text(self):
        """Prueba de error: Intenta descomprimir un texto codificado con caracteres inválidos y verifica la excepción"""
        coding = HuffmanCoding()
        with self.assertRaises(ValueError):
            coding.decode("1010abc10101")
    
    def test_encode_invalid_text_length(self):
        """Prueba de error: Intenta comprimir un texto muy corto y verifica la excepción"""
        coding = HuffmanCoding()
        with self.assertRaises(ValueError):
            coding.encode("a")

    def test_decode_invalid_encoded_data_format(self):
        """Prueba de error: Intenta descomprimir datos codificados con formato incorrecto y verifica la excepción"""
        coding = HuffmanCoding()
        with self.assertRaises(ValueError):
            coding.decode("1a0b1c0d1a0b1c0d")
    
    def test_encode_decode_simple_text(self):
        hc = HuffmanCoding()
        text = "hello"
        encoded_text = hc.encode(text)
        decoded_text = hc.decode(encoded_text)
        self.assertEqual(decoded_text, text)

    def test_encode_decode_special_characters(self):
        hc = HuffmanCoding()
        text = "!@#$%^&*"
        encoded_text = hc.encode(text)
        decoded_text = hc.decode(encoded_text)
        self.assertEqual(decoded_text, text)

    def test_encode_decode_long_text(self):
        hc = HuffmanCoding()
        text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
        encoded_text = hc.encode(text)
        decoded_text = hc.decode(encoded_text)
        self.assertEqual(decoded_text, text)

    def test_encode_decode_single_character(self):
        hc = HuffmanCoding()
        text = "aaaaaaa"
        encoded_text = hc.encode(text)
        decoded_text = hc.decode(encoded_text)
        self.assertEqual(decoded_text, text)

    def test_encode_decode_text(self):
        hc = HuffmanCoding()
        text = "hello world"
        encoded_text = hc.encode(text)
        decoded_text = hc.decode(encoded_text)
        self.assertEqual(decoded_text, text)

    def test_encode_decode_special_characters(self):
        hc = HuffmanCoding()
        text = "!@#$%^&*()"
        encoded_text = hc.encode(text)
        decoded_text = hc.decode(encoded_text)
        self.assertEqual(decoded_text, text)
        
    def test_encode_decode_mixed_case_characters(self):
        hc = HuffmanCoding()
        text = "AbCdEfGhIjKlMnOpQrStUvWxYz"
        encoded_text = hc.encode(text)
        decoded_text = hc.decode(encoded_text)
        self.assertEqual(decoded_text, text)

class ControllerTest(unittest.TestCase):
    """
        Pruebas a la Clase Controlador de la aplicación
    """

    def setUp(self):
        """ Se ejecuta siempre antes de cada metodo de prueba """
        print("Invocando setUp")
        ControladorRegistros.BorrarFilas() # Asegura que antes de cada metodo de prueba, se borren todos los datos de la tabla

    def setUpClass():
        """ Se ejecuta al inicio de todas las pruebas """
        print("Invocando setUpClass")
        ControladorRegistros.CrearTabla()  # Asegura que al inicio de las pruebas, la tabla este creada

    def tearDown(self):
        """ Se ejecuta al final de cada test """
        print("Invocnado tearDown")

    def tearDownClass():
        """ Se ejecuta al final de todos los tests """
        print("Invocando tearDownClass")

    def test_insert(self):
        """ Verifica que funcione bien la creacion y la busqueda de un usuario """
        # Pedimos crear un usuario
        print("Ejecutando testInsert")
        registro = Registro("Hola", "01011010011010110111011") 
        id = ControladorRegistros.Insertar(registro)
        registro_buscado = ControladorRegistros.BuscarPorId(id)

        # Verificamos que los datos del usuario sean correcto
        self.assertEqual(registro.decode_text, registro_buscado.decode_text)
        self.assertEqual(registro.encode_text, registro_buscado.encode_text)

    def test_update(self) :
        """
        Verifica la funcionalidad de actualizar los datos de un usuario
        """
        registro_prueba = Registro( "Hola", "01011010011010110111011") 
        id = ControladorRegistros.Insertar(registro_prueba)

        # 2. Actualizarle datos
        # usuario_prueba.cedula = "00000000" la cedula no se puede cambiar
        registro_prueba.decode_text = "Buenas"
        registro_prueba.encode_text = "001000101011100001100011101101001"
        ControladorRegistros.Actualizar(registro=registro_prueba, id=id)

        # 3. Consultarlo
        registro_actualizado = ControladorRegistros.BuscarPorId(id)

        # 4. assert
        # Verificamos que los datos del usuario sean correcto
        self.assertEqual(registro_actualizado.decode_text, registro_prueba.decode_text)
        self.assertEqual(registro_actualizado.encode_text, registro_prueba.encode_text)


    def test_delete(self):
        """ Prueba la funcionalidad de borrar usuarios """
        print("Ejecutando testDelete")
        # 1. Crear el usuario e insertarlo
        registro_prueba = Registro( "Hola", "01011010011010110111011") 
        id = ControladorRegistros.Insertar(registro_prueba)

        # 2. Borrarlo
        ControladorRegistros.Borrar(id=id)

        # 3. Buscar para verificar que no exista
        self.assertRaises(ControladorRegistros.ErrorNoEncontrado, ControladorRegistros.BuscarPorId, id=id)
    
    def test_insert_nulls(self):
        with self.assertRaises(Exception):
            ControladorRegistros.Insertar()
    
    def test_bad_id_update(self):
        #Actualiza datos que no existen
        registro_prueba = Registro("Hola", "01011010011010110111011") 
        with self.assertRaises(Exception):
            ControladorRegistros.Actualizar(registro=registro_prueba, id=100)
    
    def test_nulls_update(self):
        #Actualiza el registro con nulos
        registro_prueba = Registro( "Hola", "01011010011010110111011") 
        id = ControladorRegistros.Insertar(registro_prueba)
        with self.assertRaises(Exception):
            ControladorRegistros.Actualizar(registro=None, id=id)
    
    def test_bad_select(self):
        with self.assertRaises(Exception):
            ControladorRegistros.BuscarPorId(id=1000)
    
    def test_bad_id_delete(self):
        #Elimina un id que no existe
        with self.assertRaises(Exception):
            ControladorRegistros.Borrar(id=100)

if __name__ == '__main__':
    unittest.main()



