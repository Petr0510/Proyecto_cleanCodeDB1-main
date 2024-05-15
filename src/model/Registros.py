from datetime import date

class Registro:
    """
    Representa una cadena de texto y su respectiva codificacion
    """
    def __init__( self, decode_text, encode_text):
        
        self.decode_text = decode_text
        self.encode_text = encode_text
