import sys
sys.path.append("src")
from logica.huffman_cleanCode import HuffmanCoding
from controller import ControladorRegistros
from model.Registros import Registro



class HuffmanMenu:
    def __init__(self):
        self.huffman_coding = None

    def print_menu_options(self):
        print("\n--- Menú de Huffman Coding ---")
        print("1. Codificar texto")
        print("2. Decodificar texto")
        print("3. Consultar todos los registros")
        print("4. Modificar registro")
        print("5. Eliminar registro")
        print("6. Consultar un registro")
        print("7. Salir")

    def execute_option(self, option):
        try:
            self.huffman_coding = HuffmanCoding()
            if option == "1":
                text = input("Ingresa el texto a codificar: ")
                encoded = self.huffman_coding.encode(text=text)
                print(f"Texto original: {text}")
                print(f"Texto codificado: {encoded}")
                reg = Registro(decode_text=text, encode_text=encoded)
                ControladorRegistros.Insertar(fila=reg)
                
            elif option == "2":
                text_to_decode = input("Ingresa el texto a decodificar: ")
                decoded_text = self.huffman_coding.decode(text_to_decode)
                print(f"Texto decodificado: {decoded_text}")
                reg = Registro(decode_text=decoded_text, encode_text=text_to_decode)
                ControladorRegistros.Insertar(fila=reg)
                
            elif option == "3":
                registros = ControladorRegistros.ObtenerRegistros()
                print("Los registros actuales son:")
                for registro in registros:
                    print(f"id: {registro[0]},")
                    print(f"texto codificado: {registro[1].encode_text}")
                    print(f"texto decodificado: {registro[1].decode_text}")
                    print("-------------------------------")                
            elif option == "4":
                id_modificar = int(input("Ingresa el id del registro a modificar: "))
                print(f"Texto actual: {ControladorRegistros.BuscarPorId(id_modificar).decode_text}")
                text = input("Ingresa el texto a actualizar: ")
                encoded = self.huffman_coding.encode(text=text)
                print(f"Texto original: {text}")
                print(f"Texto codificado: {encoded}")
                reg = Registro(decode_text=text, encode_text=encoded)
                ControladorRegistros.Actualizar(registro=reg, id=id_modificar)
            elif option == "5":
                id_modificar = int(input("Ingresa el id del registro a eliminar: "))
                print(f"Texto actual a eliminar: {ControladorRegistros.BuscarPorId(id_modificar).decode_text}")
                ControladorRegistros.Borrar(id_modificar)
            elif option == "6":
                id_modificar = int(input("Ingresa el id del registro a consultar: "))
                registro = ControladorRegistros.BuscarPorId(id_modificar)
                print(f"Texto actual: {registro.decode_text}")
                print(f"Codificacion actual: {registro.encode_text}")
            elif option == "7":
                print("Saliendo del programa...")
            else:
                print("Opción no válida. Por favor, selecciona una opción válida.")
        except Exception as e:
            print(f"Error: {e}")

    def display_menu(self):
        while True:
            self.print_menu_options()
            choice = input("Selecciona una opción: ")
            self.execute_option(choice)
            if choice == "7":
                break

            input("Presiona Enter para continuar...")

if __name__ == "__main__":
    menu = HuffmanMenu()
    menu.display_menu()
