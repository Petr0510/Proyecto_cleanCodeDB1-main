"""
    Controla las operaciones de almacenamiento de la clase Registro
"""
import sys
sys.path.append("src")
from model.Registros import Registro
import psycopg2
sys.path.append('.')
import SecretConfig



class ErrorNoEncontrado( Exception ):
    """ Excepcion que indica que una fila buscada no fue encontrada"""
    pass


def ObtenerCursor() :
    """
    Crea la conexion a la base de datos y retorna un cursor para ejecutar instrucciones
    """
    DATABASE = SecretConfig.PGDATABASE
    USER = SecretConfig.PGUSER
    PASSWORD = SecretConfig.PGPASSWORD
    HOST = SecretConfig.PGHOST
    PORT = SecretConfig.PGPORT
    connection = psycopg2.connect(
        database=DATABASE,
        user=USER,
        password=PASSWORD,
        host=HOST,
        port=PORT,
        options=f"endpoint=ep-square-brook-a5llgbm5"
    )
    return connection.cursor()

def CrearTabla():
    """
    Crea la tabla de usuarios, en caso de que no exista
    """
    sql = ""
    with open("sql/crear-tablas.sql","r") as f:
        sql = f.read()        

    cursor = ObtenerCursor()
    try:
        cursor.execute(sql)
        cursor.connection.commit()
    except:
        # SI LLEGA AQUI, ES PORQUE LA TABLA YA EXISTE
        cursor.connection.rollback()

def EliminarTabla():
    """
    Borra (DROP) la tabla en su totalidad
    """    
    sql = "drop table frecuency_dictionary;"
    cursor = ObtenerCursor()
    cursor.execute( sql )
    sql = "drop table encoding_info;"
    cursor.execute( sql )
    cursor.connection.commit()

def BorrarFilas():
    """
    Borra todas las filas de la tabla (DELETE)
    ATENCION: EXTREMADAMENTE PELIGROSO.

    Si lo llama en produccion, pierde el empleo
    """
    sql = "delete from frecuency_dictionary;"
    cursor = ObtenerCursor()
    cursor.execute( sql )
    sql = "delete from encoding_info;"
    cursor.execute( sql )
    cursor.connection.commit()

def Borrar(id):
    """ Elimina la fila que contiene a un usuario en la BD """
    sql = f"delete from encoding_info where id = '{id}' RETURNING id"
    cursor = ObtenerCursor()
    cursor.execute( sql )
    id = cursor.fetchone()
    if not id:
        raise Exception (f"No se pudo eliminar el registro con id {id}")
    cursor.connection.commit()


def Insertar(fila: Registro):
    """ Guarda un Registro en la base de datos """
    try:
        # Todas las instrucciones se ejecutan a tavés de un cursor
        cursor = ObtenerCursor()
        cursor.execute(
            f"""
                insert into encoding_info (encode_text, decode_text)
                values 
                ('{fila.encode_text}',  '{fila.decode_text}') RETURNING id;
            """
        )
        nuevo_id = cursor.fetchone()[0]
        cursor.connection.commit()
        return nuevo_id
    except  :
        cursor.connection.rollback() 
        raise Exception(f"No fue posible insertar el registro {fila.decode_text}")

def BuscarPorId(id: str):    
    """ Busca un registro por el numero de id """

    # Todas las instrucciones se ejecutan a tavés de un cursor
    try:
        cursor = ObtenerCursor()
        cursor.execute(f"SELECT id, encode_text, decode_text from encoding_info where id = '{id}' ")
        fila = cursor.fetchone()
        if not fila:
            raise ErrorNoEncontrado(f"El registro buscado, no fue encontrado. id={id}")

        resultado = Registro(fila[2], fila[1])
        return resultado
    except ErrorNoEncontrado:
        raise ErrorNoEncontrado(f"El registro buscado, no fue encontrado. id={id}")
    except:
        raise Exception ("El registro no existe")
    
def ObtenerRegistros():
    """
    Obtiene todos los registros almacenados en la base de datos
    """
    try:
        cursor = ObtenerCursor()
        cursor.execute("SELECT id, encode_text, decode_text FROM encoding_info")
        registros = []
        for fila in cursor.fetchall():
            registro = Registro(fila[2], fila[1])
            registros.append((fila[0], registro))
        return registros
    except:
        raise Exception("Error al obtener los registros de la base de datos")

def ObtenerCadenaFrecuencia():
    CrearTabla()
    cursor = ObtenerCursor()
    cursor.execute(f"SELECT density_text from frecuency_dictionary limit 1")
    fila = cursor.fetchone()

    resultado = fila[0]
    return resultado

def Actualizar(registro: Registro, id: int):
    """
    Actualiza los datos de un registro en la base de datos
    """
    try:
        cursor = ObtenerCursor()
        cursor.execute(f"""
            update encoding_info
            set 
                encode_text='{registro.encode_text}',
                decode_text='{registro.decode_text}'
            where id={id} RETURNING id
        """)
        fila = cursor.fetchone()
        if not fila:
            raise Exception ("No se pudo actualizar el registro")
        cursor.connection.commit()
    except:
        raise Exception ("No se pudo actualizar el registro")

